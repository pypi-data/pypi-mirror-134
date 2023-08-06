from abc import ABC, abstractproperty
from ..common.utils import ConfigObject


class DistributorManagerConfigInterface(ConfigObject):

    @abstractproperty
    def tcp_address(self) -> str:
        """
            The public address on the network of the distributor manager
            return: a string representing the address of the distributor manager on the network
            example: tcp://127.0.0.1:1997
        """
        pass

    @abstractproperty
    def ipc_address(self) -> str:
        """
            The address that is used for interprocess communication 
            return: a string representing the address of the distributor manager inside the host
            example: ipc:///tmp/distributor_manager/0
        """
        pass
