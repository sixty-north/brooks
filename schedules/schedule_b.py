import brooks.communication

from brooks.state import State

def initial():
    return State(
        step_duration_days=1,
        num_function_points_requirements=500,
        num_function_points_developed=0,
        num_new_personnel=20,
        num_experienced_personnel=0,
        personnel_allocation_rate=0,
        personnel_assimilation_rate=0,
        assimilation_delay_days=float('inf'),
        nominal_productivity=0.1,
        new_productivity_weight=0.8,
        experienced_productivity_weight=1.2,
        training_overhead_proportion=0.0,
        communication_overhead_function=brooks.communication.no_overhead,
        software_development_rate=None,
        cumulative_person_days=0,
    )


def intervene(step_number, elapsed_time, state):
    """Intervene in the current step before the main simulation step is executed."""
    return state


def is_complete(step_number, elapsed_time_seconds, state):
    return state.num_function_points_developed >= state.num_function_points_requirements


def complete(step_number, elapsed_time_seconds, state):
    state.software_development_rate = 0
    return state

