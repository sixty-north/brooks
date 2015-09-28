from brooks.state import State


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
    while not schedule.is_complete(step_number, elapsed_time_seconds, state):
        state = schedule.intervene(step_number, elapsed_time_seconds, state)
        state = step(step_number, elapsed_time_seconds, state)
        step_number += 1
        elapsed_time_seconds += state.step_duration_days
    state = schedule.complete(step_number, elapsed_time_seconds, state)
    print("number of steps: {}".format(step_number))
    print("elapsed time: {} days".format(elapsed_time_seconds))
    print(state)


def step(step_number, elapsed_time_seconds, state):
    """Advance the simulation one time step."""

    # Determine the number of function points developed in this time-step
    delta_function_points_developed = (
        state.nominal_productivity
           * state.num_experienced_personnel * state.step_duration_days)

    state.num_function_points_developed += delta_function_points_developed
    return state

