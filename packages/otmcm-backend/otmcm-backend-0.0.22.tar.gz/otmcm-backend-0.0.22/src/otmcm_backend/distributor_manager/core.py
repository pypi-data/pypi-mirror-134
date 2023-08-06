import zmq
import logging

from otmcm_backend.distributor_manager.models import (
    ServerDistributorManagerDistributorRequestChannel,
    ServerDistributorMangerUserScriptRequestChannel
)

class DistributorManager:

    log_level: int = logging.WARNING

    def __init__(self, **kwargs) -> None:
        self._init_internal_attributes(**kwargs)

    def _init_internal_attributes(self, **kwargs):
        # Extract keyword args
        log_level = logging.DEBUG if kwargs.get("log_verbose") else logging.WARNING
        # zmq
        self.context = zmq.Context()
        # Be careful when changing the init order of these channels
        self.userscript_req_channel = ServerDistributorMangerUserScriptRequestChannel(
            context=self.context,
            logger_level=log_level
        )
        self.distributor_req_channel = ServerDistributorManagerDistributorRequestChannel(
            context=self.context,
            log_level=log_level
        )