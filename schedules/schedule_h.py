from collections import OrderedDict
import brooks.communication

from brooks.state import State

intervention_time = 0
intervention_size = 0


def configurations():
    """A series of configuration used to explore the configuration space of this scenario.

    Yields:
        Dictionaries containing keyword arguments to be passed to the configure() function.
    """
    for time in range(0, 300):
        for size in range(0, 30):
            yield OrderedDict((('time', time),
                               ('size', size)))


def configure(time, size):
    """Configure this schedule in preparation for initialisation of a run."""
    global intervention_time
    global intervention_size
    intervention_time = time
    intervention_size = size


def initial():
    """Configure the initial model state."""
    return State(
        step_duration_days=1,
        num_function_points_requirements=500,
        num_function_points_developed=0,
        num_new_personnel=7,
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
    if elapsed_time == intervention_time:
        state.num_new_personnel += intervention_size
    return state


def is_complete(step_number, elapsed_time_seconds, state):
    """Determine whether the simulation should end."""
    return state.num_function_points_developed >= state.num_function_points_requirements


def complete(step_number, elapsed_time_seconds, state):
    """Finalise the simulation state for the last recorded step."""
    state.software_development_rate = 0
    return state
