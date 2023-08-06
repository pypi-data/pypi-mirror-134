"""
Size Object
"""

from .utils import validate_list_of_strings
from .interface import send_request
from .constants import SIZES_URL

class Size:
    """Size Object Constructor

        Args:
            **kwargs: Arbitrary keyword arguments.

        Attributes:
            slug (str): A human-readable string that is used to uniquely
                identify each size.
            memory (int): The amount of RAM allocated to Droplets created
                of this size. The value is represented in megabytes.
            vcpus (int): The integer of number CPUs allocated to Droplets
                of this size.
            disk (int): The amount of disk space set aside for Droplets of
                this size. The value is represented in gigabytes.
            transfer (float): The amount of transfer bandwidth that is
                available for Droplets created in this size. This only counts
                traffic on the public interface. The value is given in
                terabytes.
            price_monthly (float): This attribute describes the monthly cost
                of this Droplet size if the Droplet is kept for an entire month.
                The value is measured in US dollars.
            price_hourly (float): This describes the price of the Droplet size
                as measured hourly. The value is measured in US dollars.
            regions (:type: list of str): An array containing the region slugs
                where this size is available for Droplet creates.
            available (bool): This is a boolean value that represents whether
                new Droplets can be created with this size.
            description (str): A string describing the class of Droplets
                created from this size. For example: Basic, General Purpose,
                CPU-Optimized, Memory-Optimized, or Storage-Optimized.

        Raises:
            ValueError - Invalid arguments
    """
    def __init__(self, **kwargs):
        #
        # Required Args
        try:
            if not isinstance(kwargs['slug'], str):
                raise ValueError("Slug must be a string")

            self.__slug = kwargs['slug']
        except KeyError as key_error:
            raise ValueError("Slug is a required argument") from key_error

        #XXX better validation here
        try:
            if not isinstance(kwargs['memory'], int) or kwargs['memory'] < 8:
                raise ValueError("Memory must be an integer >= 8")

            self.__memory = kwargs['memory']
        except KeyError as key_error:
            raise ValueError("Memory is a required argument") from key_error

        try:
            if not isinstance(kwargs['vcpus'], int) or kwargs['memory'] <1:
                raise ValueError("vcpus must be an integer > 0")

            self.__vcpus = kwargs['vcpus']
        except KeyError as key_error:
            raise ValueError("Vcpus is a required argument") from key_error


        try:
            if not isinstance(kwargs['disk'], int) or kwargs['disk'] < 0:
                raise ValueError(f"disk must be a positive integer: {kwargs['disk']}")

            self.__disk = kwargs['disk']
        except KeyError as key_error:
            raise ValueError("Disk is a required argument") from key_error

        try:
            if not isinstance(kwargs['transfer'], float) or kwargs['transfer'] < 0:
                raise ValueError(f"transfer must a float >= 1: {kwargs['transfer']}")
            self.__transfer = kwargs['transfer']
        except KeyError as key_error:
            raise ValueError("Transfer is a required argument") from key_error

        try:
            if kwargs['price_monthly'] < 0:
                raise ValueError("price_monthly must be a float > 0")

            self.__price_monthly = kwargs['price_monthly']
        except KeyError as key_error:
            raise ValueError("price_monthly is a required argument") from key_error

        try:
            if not isinstance(kwargs['price_hourly'], float) or kwargs['price_hourly'] < 0:
                raise ValueError("price_hourly must be a float > 0")

            self.__price_hourly = kwargs['price_hourly']
        except KeyError as key_error:
            raise ValueError("price_hourly is a required argument") from key_error

        try:
            validate_list_of_strings(kwargs['regions'])
        except KeyError as key_error:
            raise ValueError("Region is a required argument") from key_error
        except ValueError as value_error:
            raise ValueError("Regions must be a list of strings") from value_error

        self.__regions = kwargs['regions']

        try:
            if not isinstance(kwargs['available'], bool):
                raise ValueError("available must be a boolean")

            self.__available = kwargs['available']
        except KeyError as key_error:
            raise ValueError("avaiilable is a requied argument") from key_error

        try:
            if not isinstance(kwargs['description'], str):
                raise ValueError("description must be a string")

            self.__description = kwargs['description']
        except KeyError as key_error:
            raise ValueError("description is a required argument") from key_error


    def slug(self):
        """Size Slug Accessor

            Returns:
                slug (str): Size Slug
        """
        return self.__slug

    def memory(self):
        """Size Memory Accessor

            Returns:
                memory (int): Size Memory
        """
        return self.__memory

    def vcpus(self):
        """Size VCPUs Accessor

            Returns:
                vcpus (int): Size VCPUs
        """
        return self.__vcpus

    def disk(self):
        """Size Disk Accessor

            Returns:
                disk (int): Size Disk
        """
        return self.__disk

    def transfer(self):
        """Size Transfer

            Returns:
                transfer (float): Size float
        """
        return self.__transfer

    def price_monthly(self):
        """Size Price Montly Accessor

            Returns:
                price_montly (float): Size Price Monthly
        """
        return self.__price_monthly

    def price_hourly(self):
        """Size Price Hourly Accessor

            Returns:
                price_hourly (float): Size price hourly
        """
        return self.__price_hourly

    def regions(self):
        """Size Regions Accessor

            Returns:
                regions (:type: list of str): List of regions for size
        """
        return self.__regions

    def available(self):
        """Size Available Accessor

            Returns:
                available (bool): Size availableA
        """
        return self.__available

    def description(self):
        """Size Description Accessor

            Returns:
                description (str): Size description
        """
        return self.__description

    @classmethod
    def list_sizes(cls):
        """List Sizes

            Returns:
                sizes (:type: list of :obj: Size): List of sizes

            Raises:
                ValueError - Invalid Size
                NotAuthorized - Not Authorized to list sizes
                TooManyRequests - Too many requests made
                InternalError - Internal Error
        """
        ret = send_request("GET", SIZES_URL)

        sizes = []
        for size in ret['sizes']:
            sizes.append(Size(**size))

        return sizes
