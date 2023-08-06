"""
IPv6 Network Object
"""

class V6:
    """Network V6 Object

        Attributes:
            ip_address (str): The IP address of the IPv6 network interface.
            netmask (int): The netmask of the IPv6 network interface.
            gateway (str): The gateway of the specified IPv6 network interface.
            type (str): The type of IPv6 network interface.
                Currently IPv6 private networking is not supported.
    """
    def __init__(self, ip_address, netmask, type, gateway=None):
        self.__ip_address = ip_address
        self.__netmask = netmask
        self.__type = type
        self.__gateway = gateway

    def ip_address(self):
        """V6 IP Address Accessor

            Returns:
                ip_address (str): V6 IP Address
        """
        return self.__ip_address

    def netmask(self):
        """V6 Netmask Accessor

            Return:
                netmask (int): V6 Netmask
        """
        return self.__netmask

    def type(self):
        """V6 Type

            Return:
                type (str): V6 Type
        """
        return self.__type


    def gateway(self):
        """V6 Gateway

            Return:
                gateway (str): V6 Gateway
        """
        return self.__gateway


#XXX Need validation
