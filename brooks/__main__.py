"""Brooks.

A simulator for Brooks' Law: "Adding manpower to a late software project makes it later." (Brooks, 1975)

Usage:
    brooks <schedule>

Arguments:
    schedule    A Python module defining initial(), step() and complete() functions to control the simulation.

Options:
  -h --help     Show this screen.
  --version     Show version
"""

import sys
import importlib.machinery

from docopt import docopt

from brooks.simulation import simulate


def main(argv=None):
    if argv is None:
        argv = sys.argv

    arguments = docopt(__doc__, version="Brooks 0.5")

    schedule_file_path = arguments['<schedule>']
    loader = importlib.machinery.SourceFileLoader("schedule", schedule_file_path)
    schedule = loader.load_module()
    simulate(schedule)

    return 0

if __name__ == '__main__':
    sys.exit(main())

