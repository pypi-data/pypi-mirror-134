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
from zmq import sugar


class ServerDistributorManagerRequestChannel(OneHostDistributorMangerRequestChannel, ZMQReqRepServer):

    CHANNEL_SOCKET_PATTERN = zmq.REP

    def run_after_channel_started_tasks(self):
        # For now do nothing as this is a REP side so it just needs to wait for request and reply
        pass
        

class ServerDistributorMangerUserScriptRequestChannel(DistributorMangerUserScriptRequestChannelConfig, ZMQReqRepServer):

    CHANNEL_SOCKET_PATTERN = zmq.REP

    logger: Any
    deamon: Thread

    def _init_channel_internal_attributes(self, context: sugar.Context = None):
        super()._init_channel_internal_attributes(context=context)
        # Logging
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        # Thread
        self.deamon = Thread(target=self.run_server)

    def run_after_channel_started_tasks(self):
        super().run_after_channel_started_tasks()        
        # Run the server
        self.deamon.start()


    def generate_channel_address(self) -> str:
        address_template = super().generate_channel_address()
        # This is on server side, so just localhost binding
        return address_template.format(
            host_address="localhost"
        )
    
    def run_server(self):
        self.logger.info("DistributorManager is up and running")
        while True:
            raw_msg = self.socket.recv_json()
            self.logger.debug(raw_msg)


class DistributorRequestChannel(ZMQReqRepServer):
    pass
