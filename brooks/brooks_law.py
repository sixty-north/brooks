def step(step_number, elapsed_time, state):
    """Advance the simulation one time step.

    Args:
        step_number: An integer zero-based step number.

        elapsed_time: The elapsed time in model time units.

        state: The model state to be modified.

    Returns:
        A new model state.
    """

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
    state.software_development_rate = (
        state.nominal_productivity
        * (1 - communication_overhead)
        * (  state._new_productivity_weight * state.num_new_personnel
           + state.experienced_productivity_weight * (  state.num_experienced_personnel
                                                      - num_experienced_personnel_needed_for_training))
        * state.step_duration_days)

    state.num_function_points_developed += state.software_development_rate
    state.cumulative_person_days += state.step_duration_days * (  state.num_new_personnel
                                                                + state.num_experienced_personnel)
    return state
