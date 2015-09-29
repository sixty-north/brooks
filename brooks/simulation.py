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
        print(state)
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

    # Determine the number of new persons allocated in this time-step
    state.num_new_personnel += state.personnel_allocation_rate * state.step_duration_days

    # Determine the assimilation rate
    state.personnel_assimilation_rate = state.num_new_personnel / state.assimilation_delay_days

    # Determine the number of persons assimilated from the new personnel group
    # into the experienced personnel group
    num_assimilated = min(state.personnel_assimilation_rate * state.step_duration_days,
                          state.num_new_personnel)
    state.num_new_personnel -= num_assimilated
    state.num_experienced_personnel += num_assimilated

    # Determine the number of experienced personnel needed for training
    num_experienced_personnel_needed_for_training = state.training_overhead_proportion * state.num_new_personnel

    # Determine the communication overhead
    communication_overhead = state.communication_overhead(state.num_new_personnel + state.num_experienced_personnel)

    # Determine the number of function points developed in this time-step
    delta_function_points_developed = (
        state.nominal_productivity
        * (1 - communication_overhead)
        * (  state._new_productivity_weight * state.num_new_personnel
           + state.experienced_productivity_weight * (  state.num_experienced_personnel
                                                      - num_experienced_personnel_needed_for_training))
        * state.step_duration_days)

    state.num_function_points_developed += delta_function_points_developed
    return state



