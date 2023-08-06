import zmq

from otmcm_backend.distributor.models import (
    ClientDistributorManagerRequestChannel,
    DistributorPubSubChannel,
    DistributorRequestChannel
)

class Distributor:

    def __init__(self) -> None:
        self._init_internal_attributes()

    def _init_internal_attributes(self):
        self.context = zmq.Context()
        # Be careful when changing the init order of these channels
        self.distributor_req_channel = DistributorRequestChannel(context=self.context)
        self.pubsub_channel = DistributorPubSubChannel(context=self.context)
        self.distributor_manager_req_channel = ClientDistributorManagerRequestChannel(context=self.context)
