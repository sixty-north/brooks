import brooks.communication

from brooks.state import State

NUM_FUNCTION_POINTS_REQUIREMENTS = 500

added = False

def initial():
    """Configure the initial model state."""
    return State(
        step_duration_days=1,
        num_function_points_requirements=NUM_FUNCTION_POINTS_REQUIREMENTS,
        num_function_points_developed=0,
        num_new_personnel=22.5,
        num_experienced_personnel=0,
        personnel_allocation_rate=0,
        personnel_assimilation_rate=0,
        assimilation_delay_days=20,
        nominal_productivity=0.1,
        new_productivity_weight=0.8,
        experienced_productivity_weight=1.2,
        training_overhead_proportion=0.25,
        communication_overhead_function=brooks.communication.gompertz_overhead_proportion,
        software_development_rate=None,
        cumulative_person_days=0,
    )


def intervene(step_number, elapsed_time, state):
    """Intervene in the current step before the main simulation step is executed."""
    #if state.num_function_points_developed >= NUM_FUNCTION_POINTS_REQUIREMENTS / 2:
    #    state.num_new_personnel += 5
    #    global added
    #    added = True
    return state


def is_complete(step_number, elapsed_time_seconds, state):
    """Determine whether the simulation should end."""
    return state.num_function_points_developed >= state.num_function_points_requirements


def complete(step_number, elapsed_time_seconds, state):
    """Finalise the simulation state for the last recorded step."""
    state.software_development_rate = 0
    return state
