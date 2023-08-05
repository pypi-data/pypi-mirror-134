import zmq
import logging

from otmcm_backend.distributor_manager.models import (
    ServerDistributorManagerRequestChannel,
    ServerDistributorMangerUserScriptRequestChannel
)

class DistributorManager:

    log_level: int = logging.WARNING

    def __init__(self, *args, **kwargs) -> None:
        self._init_internal_attributes(*args, **kwargs)

    def _init_internal_attributes(self, log_verbose=False):
        # Internal
        self.log_level = logging.DEBUG if log_verbose else logging.WARNING
        # zmq
        self.context = zmq.Context()
        # Be careful when changing the init order of these channels
        self.userscript_req_channel = ServerDistributorMangerUserScriptRequestChannel(
            context=self.context,
            logger_level=self.log_level
        )
        self.distributor_req_channel = ServerDistributorManagerRequestChannel(context=self.context)        