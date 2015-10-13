"""Mapper.

Run the Brooks simulator multiple times with procedurally generated schdules.

Usage:
    mapper <schedule> [--output=<output-file>] [--] <attribute>...

Arguments:
    schedule    A Python module defining configurations(), configure(), initial(), step() and complete() functions
                to control the simulation.
    attribute   The name(s) of one or more a model state attribute(s) to be logged at the end of each run.

Options:
  --output=<output-file>  Output file: [default: stdout]
  -h --help               Show this screen.
  --version               Show version
"""

import sys
import importlib.machinery
from contextlib import contextmanager

from docopt import docopt
from brooks.brooks_law import step

from mapper.mapping import run_simulations


def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]

    arguments = docopt(__doc__, argv=argv, version="Mapper 0.5")

    schedule_file_path = arguments['<schedule>']
    loader = importlib.machinery.SourceFileLoader("schedule", schedule_file_path)
    schedule = loader.load_module()

    attributes = arguments['<attribute>']

    with open_out_stream(arguments['--output']) as output_stream:
        run_simulations(schedule, step, output_stream, attributes)

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


