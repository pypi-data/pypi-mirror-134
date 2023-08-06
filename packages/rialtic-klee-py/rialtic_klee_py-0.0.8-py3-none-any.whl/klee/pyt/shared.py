from fhir.resources.claim import Claim
from schema.insight_engine_response import InsightEngineResponse, Insight

import pytest, re
import datetime as dt
from klee.internal import Structure, log
from klee.cases import InsightEngineTestCase
from klee.files import KleeFile


with KleeFile(Structure.reference.binary, 'rb') as file:
    local_test_cases = file.read_data()
    response_cache = {}

@pytest.mark.parametrize('label, case', local_test_cases.items(), ids=local_test_cases)
class TestEngineV1:
    @pytest.fixture
    def response(self, label, case: InsightEngineTestCase, run_engine) -> InsightEngineResponse:
        log.info("Preparing to run test label %s", label)

        log.debug('Test case billable period: %s', _period(case.request.claim))
        if case.request.history:
            periods = ", ".join(_period(x.claim) for x in case.request.history)
            log.debug('Historic claim periods: %s', periods)

        if label in response_cache:
            return response_cache[label]

        response_cache[label] = run_engine(case)
        return response_cache[label]

    @pytest.fixture
    def expected(self, case: InsightEngineTestCase) -> Insight:
        return case.response.insights[0]

    @pytest.fixture
    def actual(self, label, response: InsightEngineResponse, expected: Insight) -> Insight:
        line, insight = expected.claim_line_sequence_num, None
        # todo: create a ticket on someone's board so this hack isn't needed

        log.info('Found %s insights for test label %s', len(response.insights), label)
        for ix, item in enumerate(response.insights, 1):
            prefix = f">>> Insight {ix} of {len(response.insights)}"
            if item.trace is None:
                item.trace = []

            exits = "\n\t\t".join([f"{a} <- {q}" for t in item.trace
                for q, a in (t.traversal or [])]) if item.trace else ''
            exits = "\n\t\t" + exits if exits else exits
            if ix == len(response.insights):
                exits += '\n'

            log.info('%s\n\ttype: %s, \n\tpolicy: %s \n\texit: %s %s', prefix, item.type, item.policy_name,
                " | ".join([f"{x.end_label}::{x.tree_name}" for x in item.trace]) if item.trace else '', exits)

        for item in response.insights:
            if item.claim_line_sequence_num == line:
                insight = item

        for item in response.insights:
            if item.claim_line_sequence_num == line and \
                    item.trace and item.trace[-1].end_label == label:
                insight = item

        return insight if insight else response.insights[line - 1]

    def test_insight_type(self, actual, expected):
        if actual.type == 'Error' and expected.type != 'Error':
            assert not expected.type, actual.description
        assert actual.type == expected.type

    def test_insight_description(self, actual, expected):
        if not re.search(r"{[^}]+}", expected.description):
            assert actual.description == expected.description
        else:
            assert_parameterized(actual.description, expected.description)

    def test_defense_message(self, actual, expected):
        def read_defense(x):
            msgs = x.defense.script.messages
            return msgs[0].message if msgs else ""

        actual, expected = map(read_defense, (actual, expected))
        # idk whats going on with defense remotely, but im going to view them as nuclear worthy
        normalize, scrub = lambda x: re.sub(r'[\n\r"]', "", x), lambda x: re.sub(r'[\s"]', "", x)

        try:
            assert scrub(actual) == scrub(expected)
            return
        except AssertionError:
            pass

        assert normalize(actual) == normalize(expected)

def assert_parameterized(actual, expected):
    # check for const chunks
    for chunk in re.split("{[^}]+}", expected):
        if chunk not in actual:
            assert actual == expected

    # check for replacement
    escaped = re.escape(expected)
    pattern = re.sub(r'\\{[^\\}]+\\}', "[^{].*", escaped)

    try:
        assert re.fullmatch(pattern, actual)
        return
    except AssertionError:
        pass

    # pretty printing cmp
    for var in re.findall(r"{[^}]+}", expected):
        idx = actual.find(var)
        if idx > -1:
            assert not var, actual

def _period(claim: Claim) -> str:
    return f"{_date(claim.billablePeriod.start)} - {_date(claim.billablePeriod.end)}"

def _date(date: dt.date):
    return date.strftime("%Y/%m/%d")
