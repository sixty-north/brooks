"""Brooks.

A simulator for Brooks' Law: "Adding manpower to a late software project makes it later." (Brooks, 1975)

Usage:
    brooks <schedule> [--output=<output-file>] [--] <attribute>...

Arguments:
    schedule    A Python module defining initial(), step() and complete() functions to control the simulation.
    attribute   The name(s) of one or more a model state attribute(s) to be logged at each step.

Options:
  --output=<output-file>  Output file: [default: stdout]
  -h --help               Show this screen.
  --version               Show version
"""

import sys
import importlib.machinery
from contextlib import contextmanager

from docopt import docopt

from brooks.simulation import simulate
from brooks.brooks_law import step


def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]

    arguments = docopt(__doc__, argv=argv, version="Brooks 0.5")

    schedule_file_path = arguments['<schedule>']
    loader = importlib.machinery.SourceFileLoader("schedule", schedule_file_path)
    schedule = loader.load_module()

    attributes = arguments['<attribute>']

    with open_out_stream(arguments['--output']) as output_stream:
        simulate(schedule, step, output_stream, attributes)

    return 0

@contextmanager
def open_out_stream(filepath):
    if filepath == 'stdout':
        yield sys.stdout
    else:
        f = open(filepath, 'wt')
        yield f
        f.close()

if __name__ == '__main__':
    sys.exit(main())

