class Counter:
    """
    An object for incrementally counting.
    """

    """The value counter starts from and are is reset to."""
    starting_value = 0

    # stores the current value of the counter.
    _value = starting_value

    def get_value(self):
        """
        Returns the current count.
        """
        return self._value

    def increment(self):
        """
        Increments the count by 1.
        """
        self._value += 1

    def reset(self):
        """
        Resets the count to the starting value.
        """
        self._value = self.starting_value
