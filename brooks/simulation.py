from brooks.state import State
from brooks.util import cardinal


def simulate(schedule):
    """

    Args:
        schedule: An object with the following methods:

             initial()
             intervene(step_number, elapsed_time_seconds, state)
             is_complete(step_number, elapsed_time_seconds, state)
             complete(step_number, elapsed_time_seconds, state)
    """
    args = schedule.initial()
    state = State(**args)
    step_number = 0
    elapsed_time_seconds = 0
    while True:
        state = schedule.intervene(step_number, elapsed_time_seconds, state)
        state = step(step_number, elapsed_time_seconds, state)
        if schedule.is_complete(step_number, elapsed_time_seconds, state):
            break
        step_number += 1
        elapsed_time_seconds += state.step_duration_seconds
    state = schedule.complete(step_number, elapsed_time_seconds, state)
    print("number of steps: {}".format(cardinal(step_number)))
    print("elapsed time: {} s".format(elapsed_time_seconds))
    print(state)


def step(step_number, elapsed_time_seconds, state):
    """Advance the simulation one time step."""

    # Determine the number of function points developed in this time-step
    delta_function_points_developed = (
        state.nominal_productivity
           * state.num_personnel * state.step_duration_seconds)

    state.num_function_points_developed += delta_function_points_developed
    return state

