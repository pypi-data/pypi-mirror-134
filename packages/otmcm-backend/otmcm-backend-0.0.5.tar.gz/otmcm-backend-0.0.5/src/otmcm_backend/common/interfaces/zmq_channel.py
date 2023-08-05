from abc import ABC, abstractmethod
from typing import Any
import zmq
from zmq import sugar


class ZMQChannel(ABC):

    CHANNEL_SOCKET_PATTERN: Any

    channel_address: str
    context: sugar.Context

    def __init__(self, context):
        self._init_channel_internal_attributes()
        self.start_channel()
        self.run_after_channel_started_tasks()

    def _init_channel_internal_attributes(self, context:sugar.Context=None):
        self.channel_address = self.generate_channel_address()
        self.context = context if context else zmq.Context()
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


class ZMQServer(ZMQChannel):

    def start_channel(self):
        self.socket.bind(self.channel_address)


class ZMQClient(ZMQChannel):

    def start_channel(self):
        self.socket.connect(self.channel_address)


class ZMQReqRepServer(ZMQServer):
    pass

class ZMQReqRepClient(ZMQClient):
    pass

class ZMQPubSubPublisher(ZMQServer):
    pass