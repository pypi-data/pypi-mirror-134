import zmq

from otmcm_backend.common.interfaces.zmq_channel import (
    ZMQReqRepServer,
    ZMQReqRepClient
)

from otmcm_backend.common.models.channel_models import (
    OneHostDistributorMangerRequestChannel
)


class ClientDistributorManagerRequestChannel(OneHostDistributorMangerRequestChannel, ZMQReqRepClient):

    CHANNEL_SOCKET_PATTERN = zmq.REQ

    def run_after_channel_started_tasks(self):
        # TODO: add code to inform DistributorManager of this Distributor
        pass
        


class DistributorRequestChannel(ZMQReqRepServer):
    pass

class DistributorPubSubChannel:
    pass