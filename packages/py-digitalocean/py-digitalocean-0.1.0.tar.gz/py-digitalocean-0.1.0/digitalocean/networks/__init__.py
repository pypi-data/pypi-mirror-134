"""
Networks Object
"""
from ..constants import *
from ..utils import *
from .v4 import V4
from .v6 import V6

class Networks:
    """Networks Object Constructor

        Args:
            v4 (:type: list of obj V4): List of V4 network objects
            v6 (:type: list of obj V6): List of V6 network objects


        Attributes:
            v4 (:type: list of obj V4): List of V4 network objects
            v6 (:type: list of obj V6): List of V6 network objects

        Raises:
            ValueError - Invalid Argument
    """
    def __init__(self, v4, v6):

        self.__v4 = []
        for net in v4:
            try:
                self.__v4.append(V4(**net))
            except ValueError as value_error:
                raise ValueError(
                    f"Failed to create V4 Network object: {value_error}"
                ) from value_error

        self.__v6 = []
        for net in v6:
            try:
                self.__v6.append(V6(**net))
            except ValueError as value_error:
                raise ValueError(
                    f"Failed to create V6 Network object: {value_error}"
                ) from value_error



    def v4(self):
        """Networks v4 Accessor

            Returns:
                v4 (:type: list of obj v4): List of IPv4 networks.
        """
        return self.__v4

    def v6(self):
        """Networks v6 Accessor

            Returns:
                v6 (:type: list of obj v6): List of IPv6 networks.
        """
        return self.__v6
