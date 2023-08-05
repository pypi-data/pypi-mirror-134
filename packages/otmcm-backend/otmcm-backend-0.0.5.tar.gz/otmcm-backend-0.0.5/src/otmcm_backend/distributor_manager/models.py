import zmq

from otmcm_backend.common.interfaces.zmq_channel import (
    ZMQReqRepServer
)

from otmcm_backend.common.models.channel_models import (
    OneHostDistributorMangerRequestChannel,
    DistributorMangerUserScriptRequestChannelConfig
)


class ServerDistributorManagerRequestChannel(OneHostDistributorMangerRequestChannel, ZMQReqRepServer):

    CHANNEL_SOCKET_PATTERN = zmq.REP

    def run_after_channel_started_tasks(self):
        # For now do nothing as this is a REP side so it just needs to wait for request and reply
        pass
        

class ServerDistributorMangerUserScriptRequestChannel(DistributorMangerUserScriptRequestChannelConfig, ZMQReqRepServer):

    CHANNEL_SOCKET_PATTERN = zmq.REP

    def generate_channel_address(self) -> str:
        address_template = super().generate_channel_address()
        # This is on server side, so just localhost binding
        return address_template.format(
            host_address="localhost"
        )

    


class DistributorRequestChannel(ZMQReqRepServer):
    pass
