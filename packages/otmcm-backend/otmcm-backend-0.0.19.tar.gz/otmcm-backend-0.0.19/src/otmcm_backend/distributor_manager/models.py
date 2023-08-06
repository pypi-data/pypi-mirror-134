from threading import Thread
from typing import Any
import zmq
import logging

from otmcm_backend.common.interfaces.zmq_channel import (
    ZMQReqRepServer
)

from otmcm_backend.common.models.channel_models import (
    DistributorMangerDistributorRequestChannelConfig,
    DistributorMangerUserScriptRequestChannelConfig
)
from otmcm_backend.common.models.mixsin_models import (
    MixsinLogger
)


class ServerDistributorManagerDistributorRequestChannel(DistributorMangerDistributorRequestChannelConfig, ZMQReqRepServer, MixsinLogger):

    CHANNEL_SOCKET_PATTERN = zmq.REP

    def run_worker(self):
        self.logger.info(f"DistributorManager's channel {self.__class__.__name__} is up and running")
        while True:
            raw_msg = self.socket.recv_json()
            self.logger.debug(raw_msg)
            

class ServerDistributorMangerUserScriptRequestChannel(DistributorMangerUserScriptRequestChannelConfig, ZMQReqRepServer, MixsinLogger):

    CHANNEL_SOCKET_PATTERN = zmq.REP

    def run_worker(self):
        self.logger.info(f"DistributorManager's channel {self.__class__.__name__} is up and running")
        while True:
            raw_msg = self.socket.recv_json()
            self.logger.debug(raw_msg)


class DistributorRequestChannel(ZMQReqRepServer):
    pass
