"""
Digital Ocean Droplet Modeule
"""

import re

from .constants import DROPLET_URL, VALID_DOPLET_STATUS
#AMC constants import DROPLET_URL, VALID_DOPLET_STATUS
from .interface import send_request
from .utils import validate_list_of_strings, validate_list_of_ints, validate_date_time
from .window import Window
from .image import Image
from .size import Size
from .networks import Networks
from .region import Region

class Droplet:
    """Droplet Object
        Args:
            **kwargs: Arbitrary keyword arguments.

        Attributes:
            id (int): A unique identifier for each Droplet instance.
                This is automatically generated upon Droplet creatio
            name (string): The human-readable name set for the Droplet instance.
            memory (int): Memory of the Droplet in megabytes.
            vcpus (int): The number of virtual CPUs.
            disk (int): The size of the Droplet's disk in gigabytes.
            locked (bool): A boolean value indicating whether the Droplet has been locked,
                preventing actions by users.
            status (string): A status string indicating the state of the Droplet instance.
                This may be "new", "active", "off", or "archive".
            created_at (string): A time value given in ISO8601 combined date and time format that
                represents when the Droplet was created.
            features (:type: list of str): An array of features enabled on this Droplet.
            backup_ids (:type: list of int): An array of backup IDs of any backups that have been
                taken of the Droplet instance. Droplet backups are enabled at the time
                of the instance creation.
            next_backup_window(:type: obj Window): The details of the Droplet's backups feature,
                if backups are configured for the Droplet. This object contains keys for
                the start and end times of the window during which the backup will start.
            snapshot_ids (:type: list of int): An array of snapshot IDs of any snapshots created
                from the Droplet instance.
            image (:type: obj Image): Image used to build droplet.
            volume_ids(:type: list of str): A flat array including the unique identifier
                for each Block Storage volume attached to the Droplet.
            size (:type: obj Size): Class of Droplets created from this size.
            size_slug (str): The unique slug identifier for the size of this Droplet.
            networks (:type: obj Networks): The details of the network that are configured for
                the Droplet instance. This is an object that contains keys for IPv4 and IPv6.
                The value of each of these is an array that contains objects describing
                an individual IP resource allocated to the Droplet. These will define attributes
                like the IP address, netmask, and gateway of the specific network depending on the
                type of network it is.
            region (:type: obj Region): Region the droplet resides.
            tags (:type: list of str): An array of Tags the Droplet has been tagged with.
            vpc_uuid (str, optional): A string specifying the UUID of the VPC to which the
            Droplet is assigned.

        Raises:
            ValueError: Invalid Arguments
    """
    def __init__(self, **kwargs):
        #
        # Required Args
        try:
            if not isinstance(kwargs['id'], int):
                raise ValueError(f"id must be an int: {kwargs['id']}")

            self.__id = kwargs['id']
        except KeyError as key_error:
            raise ValueError("ID is a required argument") from key_error

        try:
            if not isinstance(kwargs['name'], str):
                raise ValueError(f"Name must be a string: {kwargs['name']}")
            self.__name = kwargs['name']
        except KeyError as key_error:
            raise ValueError("Name is a required argument") from key_error

        try:
            if not isinstance(kwargs['memory'], int):
                raise ValueError(f"Memory must be an integer: {kwargs['memory']}")

            self.__memory = kwargs['memory']
        except KeyError as key_error:
            raise ValueError("Memory is a required argument") from key_error


        try:
            if not isinstance(kwargs['vcpus'], int):
                raise ValueError(f"vcpus must be an int: {kwargs['vcpus']}")

            self.__vcpus = kwargs['vcpus']
        except KeyError as key_error:
            raise ValueError("VCPUS is a required argument") from key_error


        try:
            if not isinstance(kwargs['disk'], int):
                raise ValueError(f"disk must be an int: {kwargs['disk']}")

            self.__disk = kwargs['disk']
        except KeyError as key_error:
            raise ValueError("Disk is a required argument") from key_error

        try:
            if not isinstance(kwargs['locked'], bool):
                raise ValueError(f"locked must be a bool: {kwargs['locked']}")

            self.__locked = kwargs['locked']
        except KeyError as key_error:
            raise ValueError("Locked is a required argument") from key_error


        try:
            if kwargs['status'] not in VALID_DOPLET_STATUS:
                raise ValueError(f"status not valid: {kwargs['status']}")

            self.__status = kwargs['status']
        except KeyError as key_error:
            raise ValueError("Status is a required argument") from key_error

        try:
            if not isinstance(kwargs['created_at'], str):
                raise ValueError(f"created_at must be a string: {kwargs['created_at']}")
            
            validate_date_time(kwargs['created_at'])

            self.__created_at = kwargs['created_at']
        except ValueError as value_error:
            raise ValueError("Date must be an ISO8601 formated string") from value_error
        except KeyError as key_error:
            raise ValueError("Created_at is a required argument") from key_error


        try:
            validate_list_of_strings(kwargs['features'])
            self.__features = kwargs['features']
        except ValueError as value_error:
            raise ValueError(
                f"features must be a list of strings: {kwargs['featurs']}") from value_error
        except KeyError as key_error:
            raise ValueError("Features is a required argument") from key_error

        try:
            validate_list_of_ints(kwargs['backup_ids'])
            self.__backup_ids = kwargs['backup_ids']
        except ValueError as value_error:
            raise ValueError(
                f"backup_ids must be a list of ints: {kwargs['backup_ids']}") from value_error
        except KeyError as key_error:
            raise ValueError("backup_ids is a required argument") from key_error

        try:
            if kwargs['next_backup_window'] is not None:
                window = Window(**kwargs['next_backup_window'])
                self.__next_backup_window = window
            else:
                self.__next_backup_window = None

        except ValueError as value_error:
            raise ValueError(f"Failed to create window object: {value_error}") from value_error
        except KeyError as key_error:
            raise ValueError("next_backup_window is a required argument") from key_error


        try:
            validate_list_of_ints(kwargs['snapshot_ids'])

            self.__snapshot_ids = kwargs['snapshot_ids']
        except ValueError as value_error:
            raise ValueError(
                f"snapshot_ids must be a list of ints: {kwargs['snapshot_ids']}") from value_error
        except KeyError as key_error:
            raise ValueError("snapshot_ids is a required argument") from key_error

        try:
            img = Image(**kwargs['image'])

            self.__image = img
        except ValueError as value_error:
            raise ValueError(f"Failed to create Image object: {value_error}") from value_error
        except KeyError as key_error:
            raise ValueError("Image is a required argument") from key_error


        try:
            validate_list_of_strings(kwargs['volume_ids'])

            self.__volume_ids = kwargs['volume_ids']
        except ValueError as value_error:
            raise ValueError("volume_ids must be a list of strings") from value_error
        except KeyError as key_error:
            raise ValueError("volume_ids is a required argument") from key_error

        try:
            self.__size = Size(**kwargs['size'])
        except ValueError as value_error:
            raise ValueError(f"Failed to create size object: {value_error}") from value_error
        except KeyError as key_error:
            raise ValueError("size is a required argument") from key_error

        try:
            if not isinstance(kwargs['size_slug'], str):
                raise ValueError(f"size_slug must be a str: {kwargs['size_slug']}")
            self.__size_slug = kwargs['size_slug']
        except KeyError as key_error:
            raise ValueError("size_slug is a requried argument") from key_error

        try:
            self.__networks = Networks(**kwargs['networks'])
        except ValueError as value_error:
            raise ValueError(f"Failed to create networks object: {value_error}") from value_error
        except KeyError as key_error:
            raise ValueError("networks is a required argument") from key_error

        try:
            self.__region = Region(**kwargs['region'])
        except ValueError as value_error:
            raise ValueError(f"Failed to create a region object: {value_error}") from value_error
        except KeyError as key_error:
            raise ValueError("region is a required object") from key_error

        try:
            validate_list_of_strings(kwargs['tags'])

            self.__tags = kwargs['tags']
        except ValueError as value_error:
            raise ValueError("tags must be a list of strings") from value_error
        except KeyError as key_error:
            raise ValueError("tags is a required argument") from key_error

        #
        # Optional
        if 'vpc_uuid' in kwargs:
            if not isinstance(kwargs['vpc_uuid'], str):
                raise ValueError("vpc_uusid must be a string")

            self.__vpc_uuid = kwargs['vpc_uuid']
        else:
            self.__vpc_uuid = None

    def id(self):
        """Droplet ID accessor

        Returns:
            id (int): Droplet ID
        """

        return self.__id

    def name(self):
        """Droplet Name Accessor

        Returns:
            name (str): Droplet name
        """
        return self.__name

    def memory(self):
        """Droplet Memory Accessor

        Returns:
            memory (int): Droplet Memory
        """
        return self.__memory

    def vcpus(self):
        """Droplet VCPUs Accessor

        Returns:
            vcpus (int): Droplet VCPUs
        """
        return self.__vcpus

    def disk(self):
        """Droplet Disk Accessor

        Returns:
            disk (int): Droplet Disks
        """
        return self.__disk

    def locked(self):
        """Droplet Locked Accessor

        Returns:
            locked (bool): Droplet Locked status
        """
        return self.__locked

    def status(self):
        """Droplet Status Accessor

        Returns:
            status (str): Droplet status
        """
        return self.__status

    def created_at(self):
        """Droplet Created At Accessor

        Returns:
            created_at (str): Droplet Created At time
        """
        return self.__created_at

    def features(self):
        """Droplet Features Accessor

        Returns:
            features (:type: list of str): List of droplet features.
        """
        return self.__features

    def next_backup_window(self):
        """Droplet Next Backup Window Accessor

        Returns:
            next_backup_window (:type: obj Window): Next backup window
        """
        return self.__next_backup_window

    def snapshot_ids(self):
        """Droplet Snapshot IDs Accessors

        Returns:
            snapshot_ids (:type: list of int): List of snapshot  IDs.
        """
        return self.__snapshot_ids

    def image(self):
        """Droplet Image Accessor

        Returns:
            image (:type: obj Image): Droplet Image
        """
        return self.__image

    def volume_ids(self):
        """Droplet Volume IDs Accessor

        Returns:
            volume_ids (:type: list of str): List of droplet volume Ids
        """
        return self.__volume_ids

    def size(self):
        """Droplet Size Accessor

        Returns:
            size (:type: obj Size): Droplet size information
        """
        return self.__size

    def size_slug(self):
        """Droplet Size Slug Accessor

        Returns:
            size_slug (str): Droplet Size Slug
        """
        return self.__size_slug

    def networks(self):
        """Droplet Networks Accessor

        Returns:
            networks (:type: obj Networks): Droplet Networks
        """
        return self.__networks

    def region(self):
        """Droplet Region Accessor

        Returns:
            regions (:type: obj Region): The region the droplet resides
        """
        return self.__region

    def tags(self):
        """Droplet Tags Accessor

        Returns:
            tags (:type: list of str): List of droplet tags
        """
        return self.__tags

    def vpc_uuid(self):
        """Droplet VPC UUID Accessor

        Returns:
            vpc_uuid (str): Droplet VPC UUID
        """
        return self.__vpc_uuid

    def backup_ids(self):
        """Droplet Backup IDs Accessor

        Returns:
            backup_ids (:type: list of int): List of backup ids
        """
        return self.__backup_ids

    @classmethod
    def list_droplets(cls):
        """List droplets

        Returns:
            droplets (:type: obj Droplet): List of droplet objects

        Raises:
            NotAuthorized - Request was not authorized.
            TooManyRequests - Too many requests.
            InternalError - Internal error.
        """
        ret = send_request("GET", DROPLET_URL)

        droplets = []
        for drop in ret['droplets']:
            droplets.append(Droplet(**drop))

        return droplets

    @classmethod
    def create_droplet(cls, data):
        """Create single droplet.

        Args:
            data (dict) - Dictionary representation of droplet parameters.

        Returns:
            droplet (:type: obj Droplet): Created droplet.

        Raises:
            NotAuthorized - Request was not authorized.
            TooManyRequests - Too many requests.
            InternalError - Internal error.
        """
        ret = send_request("POST", DROPLET_URL, data)

        droplet = Droplet(**ret['droplet'])

        return droplet

    @classmethod
    def get_droplet(cls, id):
        """Retrieve Droplet.

        Args:
            id (int) - Droplet ID

        Returns:
            droplet (:type: obj Droplet) - Droplet object

        Raises:
            NotAuthorized - Request was not authorized.
            NotFound - Droplet does not exist.
            TooManyRequests - Too many requests.
            InternalError - Internal error.
        """

        ret = send_request("GET", f"{DROPLET_URL}/{id}")

        droplet = Droplet(**ret['droplet'])

        return droplet

    def delete(self):
        """Delete an existing droplet.

        Returns:
            True - Droplet was deleted

        Raises:
            NotAuthorized - Request was not authorized.
            NotFound - Droplet does not exist.
            TooManyRequests - Too many requests.
            InternalError - Internal error.
        """
        send_request("DELETE", f"{DROPLET_URL}/{self.__id}")

        return True
