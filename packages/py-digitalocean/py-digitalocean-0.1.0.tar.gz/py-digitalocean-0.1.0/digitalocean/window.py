"""
Window Object
"""
class Window:
    """Window Object Constructor

        Attributes:
            start (str): A time value given in ISO8601 combined date and time
                format specifying the start of the Droplet's backup window.
            end (str): A time value given in ISO8601 combined date and time
                format specifying the end of the Droplet's backup window.

        Raises:
            ValueError: Invalid arguments
    """
    def __init__(self, start, end):
        #XXX better validation
        if not isinstance(start, str):
            raise ValueError("Start must be a string")

        self.__start = start

        if not isinstance(end, str):
            raise ValueError("End must be a string")

        self.__end = end

    def start(self):
        """Window Start Accessor

            Returns:
                start (str): Backup window start time
        """
        return self.__start

    def end(self):
        """Window End Accessor

            Returns:
                end (str): Backup window wend time
        """
        return self.__end
