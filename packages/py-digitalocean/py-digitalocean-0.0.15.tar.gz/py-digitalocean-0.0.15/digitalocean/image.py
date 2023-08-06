"""
    Digital Ocean Image Module
"""
from .constants import VALID_DIST_TYPES, VALID_IMAGE_TYPES, VALID_IMAGE_STATUS
from .utils import validate_list_of_strings, validate_date_time

class Image:
    """Digital Ocean Image Object

        Args:
            **kwargs: Arbitrary keyword arguments.

        Attributes:
            name (str): The display name that has been given to an image.
            distribution (str): The name of a custom image's distribution.
            public (bool): This is a boolean value that indicates whether
                the image in question is public or not.
            regions (:obj:list of str): This attribute is an array of the regions that
                the image is available in. The regions are represented by their
                identifying slug values.
            id (int, optional): A unique number that can be used to identify and reference
            a specific image.
            type (int, optional): Describes the kind of image. It may be one of "snapshot",
                "backup", or "custom". This specifies whether an image is a user-generated
                Droplet snapshot, automatically created Droplet backup, or a user-provided
                virtual machine image.
            created_at (str, optional): A time value given in ISO8601 combined date and time
                format that represents when the image was created.
            slug (str, optional): A uniquely identifying string that is associated with each of the
                DigitalOcean-provided public images. These can be used to reference a public
                image as an alternative to the numeric id
            created_at (str, optional): A time value given in ISO8601 combined date and time format
                that represents when the image was created.
            min_disk_size (str, optional): The minimum disk size in GB required for a
                Droplet to use this image.
            size_gigabyes (float, optional): The size of the image in gigabytes.
            description (str, optional): An optional free-form text field to describe an image.
            tags (:type: list of str, optional): A flat array of tag names as strings to be applied
                to the resource.  Tag names may be for either existing or new tags.
            status (:type: list of str, optional): A status string indicating
                the state of a custom image. This may be NEW, available,
                pending, deleted, or retired.

        Raises:
            ValueError - Invalid arguments
    """
    def __init__(self, **kwargs):

        #TODO: Make common validation functions

        #
        # Required Args
        try:
            if not isinstance(kwargs['name'], str):
                raise ValueError("Name must be a string")
            self.__name = kwargs['name']
        except KeyError as key_error:
            raise ValueError("Name is a required argument") from key_error

        try:
            if kwargs['distribution'] not in VALID_DIST_TYPES:
                raise ValueError(f"Image distribution must be one of: {VALID_DIST_TYPES}")
            self.__distribution = kwargs['distribution']
        except KeyError as key_error:
            raise ValueError("Distribution is a required argument") from key_error

        try:
            if not isinstance(kwargs['public'], bool):
                raise ValueError("Public must be a boolean")
            self.__public = kwargs['public']
        except KeyError as key_error:
            raise ValueError("Public is a required argument") from key_error

        try:
            validate_list_of_strings(kwargs['regions'])
        except KeyError as key_error:
            raise ValueError("Region is a required argument") from key_error
        except ValueError as value_error:
            raise ValueError("Regions must be a list of strings") from value_error
        self.__regions = kwargs['regions']


        #
        # Optional Args
        if 'id' in kwargs:
            if not isinstance(kwargs['id'], int):
                raise ValueError("ID must be an integer")
            self.__id = kwargs['id']
        else:
            self.__id = None

        if 'type' in kwargs:
            if kwargs['type'] not in VALID_IMAGE_TYPES:
                raise ValueError(f"Invalid Image Type: {kwargs['type']}")
            self.__type = kwargs['type']
        else:
            self.__type = None

        if 'slug' in kwargs:
            if not isinstance(kwargs['slug'], str):
                raise ValueError(f"Image Slug must be a string: {kwargs['slug']}")
            self.__slug = kwargs['slug']
        else:
            self.__slug = None

        if 'created_at' in kwargs:
            if not isinstance(kwargs['created_at'], str):
                raise ValueError("created_at must be a string")

            try:
                validate_date_time(kwargs['created_at'])
            except ValueError as value_error:
                raise ValueError("Date must be an ISO8601 formated string") from value_error
            self.__created_at = kwargs['created_at']
        else:
            self.__created_at = None

        if 'min_disk_size' in kwargs:
            if not isinstance(kwargs['min_disk_size'], int) or kwargs['min_disk_size'] < 0:
                raise ValueError("Min Disk Size must be an integer >= 0")
            self.__min_disk_size = kwargs['min_disk_size']
        else:
            self.__min_disk_size = None

        if 'size_gigabytes' in kwargs:
            if not isinstance(kwargs['size_gigabytes'], float):
                raise ValueError("Image gigabyte size must be a float")
            self.__size_gigabytes = kwargs['size_gigabytes']
        else:
            self.__size_gigabytes = None

        if 'description' in kwargs:
            if not isinstance(kwargs['description'], str):
                raise ValueError("Description must be a string")
            self.__description = kwargs['description']
        else:
            self.__description = None

        if 'tags' in kwargs:
            try:
                validate_list_of_strings(kwargs['tags'])
            except ValueError as value_error:
                raise ValueError("Tags must be a list of strings") from value_error
            self.__tags = kwargs['tags']
        else:
            self.__tags = []

        if 'status' in kwargs:
            if kwargs['status'] not in VALID_IMAGE_STATUS:
                raise ValueError(f"Status must be one of the following: {VALID_IMAGE_STATUS}")
            self.__status = kwargs['status']
        else:
            self.__status = None

    def id(self):
        """Image ID Accessor

            Returns:
                id (int): Image ID.
        """
        return self.__id

    def name(self):
        """Image Name Accessor

            Returns:
                name (str): Image Name
        """
        return self.__name

    def type(self):
        """Image Type Accessor

            Returns:
                type (str): Image type
        """
        return self.__type

    def distribution(self):
        """Image Distribution Accessor

            Returns:
                distribution (str): Image distribution
        """
        return self.__distribution

    def slug(self):
        """Image Slug Accessor

            Returns:
                slug (str): Image slug
        """
        return self.__slug

    def public(self):
        """Image Public Accessor

            Returns:
                public (bool): Image public status
        """
        return self.__public

    def regions(self):
        """Image Regions Accessor

            Returns:
                regions (:type: list of str): List of regions the image is available in.
        """
        return self.__regions

    def created_at(self):
        """Image Created at Accessor

            Returns:
                created_at (str): Image created at time
        """
        return self.__created_at

    def min_disk_size(self):
        """Image Min Disk Size Accessor

            Returns:
                min_disk_size (int): Image minimum disk size
        """
        return self.__min_disk_size

    def size_gigabytes(self):
        """Image Size in gigabytes Accessor

            Returns:
                size_gigabytes (float): Image size in gigabytes
        """
        return self.__size_gigabytes

    def description(self):
        """Image description Accessor

            Returns:
                description (str): Image description
        """
        return self.__description

    def tags(self):
        """Image Tags Accessor

            Returns:
                tags (:type: list of str): List of Image tags.
        """
        return self.__tags

    def status(self):
        """Image Status Accessor

            Returns:
                status (str): Image status.
        """
        return self.__status
