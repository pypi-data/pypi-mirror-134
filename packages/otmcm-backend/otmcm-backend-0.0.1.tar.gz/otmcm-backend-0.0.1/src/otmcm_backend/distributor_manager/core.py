import zmq

from otmcm_backend.distributor_manager.models import (
    ServerDistributorManagerRequestChannel,
    ServerDistributorMangerUserScriptRequestChannel
)

class DistributorManager:
    def __init__(self) -> None:
        self._init_internal_attributes()

    def _init_internal_attributes(self):
        self.context = zmq.Context()
        # Be careful when changing the init order of these channels
        self.userscript_req_channel = ServerDistributorMangerUserScriptRequestChannel(context=self.context)
        self.distributor_req_channel = ServerDistributorManagerRequestChannel(context=self.context)