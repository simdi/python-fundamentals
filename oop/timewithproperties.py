# timewithproperties.py
"""Time class definition."""
from datetime import datetime

class Time:
    """
      Time class for maintaining a time of day.
      Attributes:
        hour: The hour of the day.
        minute: The minute of the hour.
        second: The second of the minute.
    """

    def __init__(self, hour=0, minute=0, second=0):
        """Initialize the Time object."""
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        """Return a string representation of the Time object."""
        return f"{self._hour:02d}:{self._minute:02d}:{self._second:02d}"

    def __repr__(self):
        """Return a string representation of the Time object."""
        return f"Time(hour={self._hour}, minute={self._minute}, second={self._second})"

    def __eq__(self, other):
        """Return True if the times are equal."""
        return self._hour == other.hour and self._minute == other.minute and self._second == other.second

    def __lt__(self, other):
        """Return True if the time is less than other."""
        if self._hour < other.hour:
            return True
        if self._hour > other.hour:
            return False
        if self._minute < other.minute:
            return True
        if self._minute > other.minute:
            return False
        if self._second < other.second:
            return True
        return False

    def __gt__(self, other):
        """Return True if the time is greater than other."""
        if self._hour > other.hour:
            return True
        if self._hour < other.hour:
            return False
        if self._minute > other.minute:
            return True
        if self._minute < other.minute:
            return False
        if self._second > other.second:
            return True
        return False

    @property
    def hour(self):
        """Return the hour of the day."""
        return self._hour

    @hour.setter
    def hour(self, hour):
        """Set the hour of the day."""
        if hour < 0 or hour > 23:
            raise ValueError("Hour must be between 0 and 23")
        self._hour = hour

    @property
    def minute(self):
        """Return the minute of the hour."""
        return self._minute

    @minute.setter
    def minute(self, minute):
        """Set the minute of the hour."""
        if minute < 0 or minute > 59:
            raise ValueError("Minute must be between 0 and 59")
        self._minute = minute


    @property
    def second(self):
        """Return the second of the minute."""
        return self._second

    @second.setter
    def second(self, second):
        """Set the second of the minute."""
        if second < 0 or second > 59:
            raise ValueError("Second must be between 0 and 59")
        self._second = second

    def set_time(self, hour=0, minute=0, second=0):
        """Set the time."""
        self.hour = hour
        self.minute = minute
        self.second = second

        