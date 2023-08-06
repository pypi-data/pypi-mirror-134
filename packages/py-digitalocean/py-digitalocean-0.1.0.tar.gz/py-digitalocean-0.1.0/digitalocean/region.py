"""
Region Object
"""

###########
# Imports #
# #########
from .utils import validate_list_of_strings
from .interface import send_request
from .constants import REGIONS_URL

class Region:
    """Region Object Constructor

        Attributes:
            name (str): The display name of the region. This will be a
                full name that is used in the control panel and other interfaces.
            slug (str): A human-readable string that is used as a unique
                identifier for each region.
            features (:type: list of str): This attribute is set to an array
                which contains features available in this region
            available (bool): This is a boolean value that represents whether
                new Droplets can be created in this region.
            sizes (:type: list of str): This attribute is set to an array
                which contains the identifying slugs for the sizes available in this region.

        Rasies:
            ValueError - Invalid arguments
    """
    def __init__(self, name, slug, features, available, sizes):

        if not isinstance(name, str):
            raise ValueError("Name must be a string")

        self.__name = name

        if not isinstance(slug, str):
            raise ValueError("Slug must be a string")

        self.__slug = slug

        try:
            validate_list_of_strings(features)
        except ValueError as value_error:
            raise ValueError("Features must be a list of strings") from value_error

        self.__features = features

        if not isinstance(available, bool):
            raise ValueError("Available must be a boolean")

        self.__available = available

        try:
            validate_list_of_strings(sizes)
        except ValueError as value_error:
            raise ValueError("Sizes must be a list of strings") from value_error
        self.__sizes = sizes

    def name(self):
        """Region Name Accessor

            Returns:
                name (str): Region Name
        """
        return self.__name

    def slug(self):
        """Region Slug Accessor

            Returns:
                slug (str): Region Slug
        """
        return self.__slug

    def features(self):
        """Region Features Accessor

            Returns:
                features (:type: list of str): Region features
        """
        return self.__features

    def available(self):
        """Region Availble Accessor

            Returns:
                available (bool): Region Availability
        """
        return self.__available

    def sizes(self):
        """Region Sizes Accessor

            Returns:
                sizes (:type: list of str): Region sizes
        """
        return self.__sizes

    @classmethod
    def list_regions(cls):
        """List Regions

            Returns:
                regions (:type: obj Region): List of regions

            Raises:
                ValueError - Failed to create region object
                NotAuthorized - Request was not authorized.
                TooManyRequests - Too many requests.
                InternalError - Internal error.
        """
        ret = send_request("GET", REGIONS_URL)

        regions = []
        for reg in ret['regions']:
            regions.append(Region(**reg))

        return regions
