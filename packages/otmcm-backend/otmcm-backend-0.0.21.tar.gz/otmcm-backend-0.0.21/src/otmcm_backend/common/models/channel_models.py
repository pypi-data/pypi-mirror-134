from typing import Union
import zmq

from otmcm_backend.common.interfaces.zmq_channel import (
    ZMQReqRepClient
)


class TcpChannelConfig:
    # The port will be used for this channel
    CONNECT_PORT:Union[int, None]=None

    def generate_channel_address(self)->str:
        if self.CONNECT_PORT is None:
            raise Exception("CONNECT_PORT need to be defined")
        else:
            return f"tcp://{{host_address}}:{self.CONNECT_PORT}"



class OneHostDistributorMangerRequestChannel(TcpChannelConfig):
    """This class represents the DistributorMangerRequestChannel for the case
    Distributor and DistributorManager run on one host, which means, both Distributor and
    DistributorManager only need to bind their socket to the address
    tcp://127.0.0.1:port
    However, if Distributor and DistributorManager are on different hosts, then the binding
    address could be different for each side. For now, this class assuming both are on the same host
    
    # TODO - Solve the case when distributor is not on the same host?

    """

    def generate_channel_address(self)->str:
        address_template = super().generate_channel_address()
        # Assuming the distributor manager is in the same host so
        return address_template.format(
            host_address="127.0.0.1"
        )

class DistributorMangerDistributorRequestChannelConfig(OneHostDistributorMangerRequestChannel):
    # The port will be used for this channel
    CONNECT_PORT:int = 5551
    
class DistributorMangerUserScriptRequestChannelConfig(OneHostDistributorMangerRequestChannel):
    # The port will be used for this channel
    CONNECT_PORT:int = 1997