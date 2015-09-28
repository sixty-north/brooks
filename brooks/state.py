class State:
    """Aggegated instantaneous state of the simulation."""

    def __init__(
            self,
            step_duration_seconds,
            num_function_points_requirements,
            num_function_points_developed,
            num_experienced_personnel,
            nominal_productivity):
        self.step_duration_seconds = step_duration_seconds
        self.num_function_points_requirements = num_function_points_requirements
        self.num_function_points_developed = num_function_points_developed
        self.num_experienced_personnel = num_experienced_personnel
        self.nominal_productivity = nominal_productivity
        pass

    @property
    def step_duration_seconds(self):
        return self._step_duration_seconds

    @step_duration_seconds.setter
    def step_duration_seconds(self, value):
        if value <= 0:
            raise ValueError("Step duration {!r} must be positive".format(value))
        self._step_duration_seconds = value

    @property
    def num_function_points_requirements(self):
        return self._num_function_points_requirements

    @num_function_points_requirements.setter
    def num_function_points_requirements(self, value):
        if value < 0:
            raise ValueError("Number of required function points {0} cannot be negative".format(value))
        self._num_function_points_requirements = value

    @property
    def num_function_points_developed(self):
        return self._num_function_points_developed

    @num_function_points_developed.setter
    def num_function_points_developed(self, value):
        if value < 0:
            raise ValueError("Number of developed function points {0} cannot be negative".format(value))
        self._num_function_points_developed = value

    @property
    def num_experienced_personnel(self):
        return self._num_experienced_personnel

    @num_experienced_personnel.setter
    def num_experienced_personnel(self, value):
        if value < 0:
            raise ValueError("Number of personnel {0} cannot be negative".format(value))
        self._num_experienced_personnel = value

    @property
    def nominal_productivity(self):
        """Nominal productivity in function points per person per second."""
        return self._nominal_productivity

    @nominal_productivity.setter
    def nominal_productivity(self, value):
        if value <= 0:
            raise ValueError("Nominal productivity {0} function-points/person/second must be positive".format(value))
        self._nominal_productivity = value

    def __repr__(self):
        return "{}("                                 \
            "step_duration_seconds={}, "             \
            "num_functions_points_requirements={}, " \
            "num_functions_points_developed={}, "    \
            "num_experienced_personnel={}, "         \
            "nominal_productivity={}"                \
            ")".format(
                self.__class__.__name__,
                self._step_duration_seconds,
                self._num_function_points_requirements,
                self._num_function_points_developed,
                self._num_experienced_personnel,
                self._nominal_productivity
            )