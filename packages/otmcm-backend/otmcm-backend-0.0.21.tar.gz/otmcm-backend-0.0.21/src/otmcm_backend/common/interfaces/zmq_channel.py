from abc import ABC, abstractmethod
import logging
from threading import Thread
from typing import Any
import zmq
from zmq import sugar

from otmcm_backend.common.models.mixsin_models import MixsinLogger


class ZMQChannel(ABC):

    CHANNEL_SOCKET_PATTERN: Any

    channel_address: str
    context: sugar.Context

    def __init__(self, **kwarg):
        self._init_channel_internal_attributes(**kwarg)
        self.start_channel()
        self.run_after_channel_started_tasks()

    def _init_channel_internal_attributes(self, **kwarg):
        # Extract args
        context = kwarg.get("context") if kwarg.get("context") else zmq.Context()
        # Init
        self.channel_address = self.generate_channel_address()
        self.context = context 
        self.socket = self.context.socket(self.CHANNEL_SOCKET_PATTERN)

    @abstractmethod
    def start_channel(self):
        """
        Child classes need to implement this method to bind
        the socket to bind or connect socket
        """
        pass
    
    @abstractmethod
    def generate_channel_address(self)->str:
        """
        Child class need to implement this function to generate the address
        the socket will bind to
        """
        pass

    
    def run_after_channel_started_tasks(self):
        """Child class should overwrite this method when it needs to run something 
        once the channel has been set up
        """
        pass

class ZMQChannelWithWorker(ZMQChannel):

    channel_worker: Thread

    def _init_channel_internal_attributes(self, **kwarg):
        super()._init_channel_internal_attributes(**kwarg)
        self.channel_worker = Thread(target=self.run_worker)
    
    def run_after_channel_started_tasks(self):
        super().run_after_channel_started_tasks()
        # Run the worker
        self.channel_worker.start()

    @abstractmethod
    def run_worker(self):
        """Child class need to define how the channel interpret message or run worker here
        """
        pass

class ZMQChannelWithWorkerNLogger(ZMQChannelWithWorker, MixsinLogger):

    def _init_channel_internal_attributes(self, **kwarg):
        super()._init_channel_internal_attributes(**kwarg)
        # Extract args
        log_level = kwarg.get("logger_level") if kwarg.get("logger_level") else logging.WARNING
        # Set up Logging
        self.set_up_logger(log_level=log_level)



class ZMQServer(ZMQChannelWithWorkerNLogger):

    def start_channel(self):
        self.socket.bind(self.channel_address)


class ZMQClient(ZMQChannelWithWorkerNLogger):

    def start_channel(self):
        self.socket.connect(self.channel_address)


class ZMQReqRepServer(ZMQServer):    
    pass

class ZMQReqRepClient(ZMQClient):
    pass

class ZMQPubSubPublisher(ZMQServer):
    pass