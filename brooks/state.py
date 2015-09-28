class State:
    """Aggegated instantaneous state of the simulation."""

    def __init__(
            self,
            step_duration_seconds,
            num_function_points_requirements,
            num_function_points_developed,
            num_personnel,
            development_rate_function_points_per_person_per_second):
        self.step_duration_seconds = step_duration_seconds
        self.num_function_points_requirements = num_function_points_requirements
        self.num_function_points_developed = num_function_points_developed
        self.num_personnel = num_personnel
        self.development_rate_function_points_per_person_per_second = development_rate_function_points_per_person_per_second
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
    def num_personnel(self):
        return self._num_personnel

    @num_personnel.setter
    def num_personnel(self, value):
        if value < 0:
            raise ValueError("Number of personnel {0} cannot be negative".format(value))
        self._num_personnel = value

    @property
    def development_rate_function_points_per_person_per_second(self):
        return self._development_rate_function_points_per_person_per_second

    @development_rate_function_points_per_person_per_second.setter
    def development_rate_function_points_per_person_per_second(self, value):
        if value <= 0:
            raise ValueError("Development rate {0} must be positive".format(value))
        self._development_rate_function_points_per_person_per_second = value

    def __repr__(self):
        return "{}("                                 \
            "step_duration_seconds={}, "             \
            "num_functions_points_requirements={}, " \
            "num_functions_points_developed={}, "    \
            "num_personnel={}"                       \
            ")".format(
                self.__class__.__name__,
                self._step_duration_seconds,
                self._num_function_points_requirements,
                self._num_function_points_developed,
                self._num_personnel
            )