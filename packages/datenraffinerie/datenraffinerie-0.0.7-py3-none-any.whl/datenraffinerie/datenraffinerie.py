import click
from .valve_yard import ValveYard
from .config_utilities import ConfigFormatError DAQConfigError
import logging

@click.command()
@click.argument('config', type=click.Path(exists=True))
@click.argument('procedure', type=str)
@click.argument('output', type=click.Path)
@click.option('-w', '--workers', 'workers', type=int, default=4)
def cli(config, procedure, workers):
    try:
        RUN_RESULT = luigi.build([ValveYard(
            click.fromat_filename(config),
            procedure,
            output)],
            local_scheduler=True,
            workers=workers,
            resources={'hexacontroller': 1}
            )
    except ConfigFormatError as e:
        print(e.message)
        exit(1)
    except DAQConfigError as e:
        print("The Configuration of one of the executed DAQ procedures is malformed: ")
        print(e.message)
        exit(1)
    except Exception as e:
        print("An error occured that was not properly caught")
        print(e)
        exit(1)
