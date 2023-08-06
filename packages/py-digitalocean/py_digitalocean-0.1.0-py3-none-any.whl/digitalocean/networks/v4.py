"""
IPv4 Network Object
"""
class V4:
    """V4 Network Object

        Attributes:
            ip_address (str): The IPv4 network interface
            netmask (str): The netmask of the IPv4 network interface
            gateway (str): The gateway of the specified IPv4 network interface.
                For private interfaces, a gateway is not provided.
            type (str): The type of IPv4 network interface (public, private)
    """
    def __init__(self, ip_address, netmask, type, gateway=None):
        #XXX need validation
        self.__ip_address = ip_address
        self.__netmask = netmask
        self.__type = type
        self.__gateway = gateway

    def ip_address(self):
        """V4 IP Address Accessor

            Returns:
                ip_address (str): IPv4 Address
        """
        return self.__ip_address

    def netmask(self):
        """V4 IP Netmask Accessor

            Returns:
                netmask (str): IPv4 Netmask
        """
        return self.__netmask

    def type(self):
        """V4 Type

            Returns:
                type (str): IPv4 type (public|private)
        """
        return self.__type


    def gateway(self):
        """V4 Gateway

            Returns:
                gateway (str): IPv4 gateway
        """
        return self.__gateway
