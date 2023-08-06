import click

from .app import App
from . import __version__

@click.command()
@click.version_option(version=__version__)
@click.option('--machine', help='(WORK IN PROGRESS) Display load on specific machine.')
@click.option('--cluster', help='Overview of the cluster usage.', is_flag=True)
def main(machine, cluster):
    """
    Command line tool to display the current usage of machines on our local cluster.
    """

    if machine:
        print('This function still needs to be implemented.\n')
    elif cluster:
        App.run()
    else:
        App.run()
        # print(
        #     "At least one input must be provided.\n\n"
        #     "Usage: machine_usage [OPTIONS]\n"
        #     "Try 'machine_usage --help' for help."
        # )
