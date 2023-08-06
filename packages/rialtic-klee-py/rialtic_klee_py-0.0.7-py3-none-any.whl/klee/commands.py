import click, os, sys, traceback
from klee.internal import log, Structure
from klee import plans, test

@click.group()
def cli():
    if not os.path.exists('oim-engine.json'):
        print("This utility may only be run from within an engine's root directory.")
        sys.exit(0)

@cli.command('build')
@click.argument('targets', nargs = -1)
@click.option('-p', '--plan-type', default = 'default',
    type = click.Choice([*plans.Options], case_sensitive = False))
@click.option('-c', '--claims-dir', default = 'test_claims', help='suggested location: test_claims')
@click.option('-o', '--output-dir', default = 'test_cases', help="suggested location: test_cases")
def BuildCommand(targets, plan_type, claims_dir, output_dir):
    structure = Structure(os.getcwd(), claims_dir, output_dir)
    structure.json_enabled = True; structure.register_instance()
    _echo('Building', targets)

    @error_logging
    def _logic():
        build_sys = plans.Options[plan_type.lower()](structure)
        build_sys.build_node_labels(targets)

def klee_test_decorate(fn):
    click.argument('targets', nargs=-1)(fn)
    click.option('-p', '--plan_type', default='default', type =
        click.Choice([*plans.Options], case_sensitive=False))(fn)
    click.option('-c', '--claims-dir', default='test_claims', help='suggested location: test_claims')(fn)
    click.option('-o', '--output-dir', default='test_cases', help="suggested location: test_cases")(fn)
    click.option('--pytest', default = "-vvv", help="arguments to send to pytest")(fn)

@klee_test_decorate
@cli.command('test')
def ExecLocalTest(targets, plan_type, claims_dir, output_dir, pytest):
    structure = Structure(os.getcwd(), claims_dir, output_dir)
    structure.register_instance()

    _echo('Running tests for', targets)
    if not test.PyTestUtility.env_vars_present():
        return print("aborting...")

    @error_logging
    def _logic():
        build_sys = plans.Options[plan_type.lower()](structure)
        test_cases = build_sys.build_node_labels(targets)

        args = [x.strip() for x in pytest.split(',')]
        test.LocalTest(args).invoke_cases(test_cases)

@klee_test_decorate
@cli.command('smoke')
def ExecSmokeTest(targets, plan_type, claims_dir, output_dir, pytest):
    structure = Structure(os.getcwd(), claims_dir, output_dir)
    structure.register_instance(); _echo('Running smoke tests for', targets)

    @error_logging
    def _logic():
        build_sys = plans.Options[plan_type.lower()](structure)
        test_cases = build_sys.build_node_labels(targets)

        args = [x.strip() for x in pytest.split(',')]
        test.SmokeTest(args).invoke_cases(test_cases)


def _echo(what, targets):
    message = f'cli: {what} {",".join(targets) or "all"} targets\n'
    click.echo(message); log.info(message)

def error_logging(closure):
    try:
        closure()
    except:
        log.critical(traceback.format_exc())
