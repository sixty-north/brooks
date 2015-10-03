from collections import OrderedDict
from itertools import chain

from brooks.state import State


def simulate(schedule, step, output_stream=None, attributes=tuple()):
    """

    Args:
        schedule: An object with the following methods:

             initial()
             intervene(step_number, elapsed_time, state)
             is_complete(step_number, elapsed_time, state)
             complete(step_number, elapsed_time, state)

        step: A function used to update the model state with each
            step. It must have the signature:

                step(step_number, elapsed_time, state)

        output_stream: A file-like object to which results will be streamed.

        attributes: An iterable series of attribute names to be recorded in the output stream.

    """
    state = schedule.initial()
    step_number = 0
    elapsed_time = 0
    write_tsv_header(output_stream, attributes)
    while not schedule.is_complete(step_number, elapsed_time, state):
        write_tsv_record(output_stream, step_number, elapsed_time, state, attributes)
        state = schedule.intervene(step_number, elapsed_time, state)
        state = step(step_number, elapsed_time, state)
        step_number += 1
        elapsed_time += state.step_duration_days
    state = schedule.complete(step_number, elapsed_time, state)
    write_tsv_record(output_stream, step_number, elapsed_time, state, attributes)

def write_tsv_header(output_stream, attributes):
    default_columns = ['step_number', 'elapsed_time']
    header = '\t'.join(chain(default_columns, attributes))
    print(header, file=output_stream)

def write_tsv_record(output_stream, step_number, elapsed_time, state, attributes):
    """Record the model state to a stream.

    Args:
        output_stream: A file-like object to which results will be streamed.
        step_number: An integer step number.
        elapsed_time: The elapsed model time.
        state: The current model state.
        attributes: An iterable series of attribute names from the state object to be recorded.
    """
    fields = OrderedDict()
    fields['step_number'] = str(step_number)
    fields['elapsed_time'] = str(elapsed_time)

    for attribute in attributes:
        field = str(getattr(state, attribute))
        if '\t' in field:
            raise ValueError('Field value {!r} contains a tab character. Cannot write to TSV file.'.format(field))
        fields[attribute] = field

    line = '\t'.join(fields.values())
    print(line, file=output_stream)
