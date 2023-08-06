from threading import Thread
from typing import Any
import zmq
import logging

from otmcm_backend.common.interfaces.zmq_channel import (
    ZMQReqRepServer
)

from otmcm_backend.common.models.channel_models import (
    OneHostDistributorMangerRequestChannel,
    DistributorMangerUserScriptRequestChannelConfig
)
from otmcm_backend.common.models.mixsin_models import (
    MixsinLogger
)


class ServerDistributorManagerRequestChannel(OneHostDistributorMangerRequestChannel, ZMQReqRepServer):

    CHANNEL_SOCKET_PATTERN = zmq.REP

    def run_after_channel_started_tasks(self):
        # For now do nothing as this is a REP side so it just needs to wait for request and reply
        pass
        

class ServerDistributorMangerUserScriptRequestChannel(DistributorMangerUserScriptRequestChannelConfig, ZMQReqRepServer, MixsinLogger):

    CHANNEL_SOCKET_PATTERN = zmq.REP

    logger: Any
    logger_level: int
    deamon: Thread

    def _init_channel_internal_attributes(self, **kwarg):
        super()._init_channel_internal_attributes(**kwarg)
        # Extract args
        log_level = kwarg.get("logger_level") if kwarg.get("logger_level") else logging.WARNING
        # Set up Logging
        self.set_up_logger(log_level=log_level)
        # Thread
        self.deamon = Thread(target=self.run_server)



    def run_after_channel_started_tasks(self):
        super().run_after_channel_started_tasks()        
        # Run the server
        self.deamon.start()


    def generate_channel_address(self) -> str:
        address_template = super().generate_channel_address()
        # This is on server side, so just 127.0.0.1 binding
        return address_template.format(
            host_address="127.0.0.1"
        )
    
    def run_server(self):
        self.logger.info(f"[DistributorManager's channel {self.__class__.__name__} is up and running")
        while True:
            raw_msg = self.socket.recv_json()
            self.logger.debug(raw_msg)


class DistributorRequestChannel(ZMQReqRepServer):
    pass
