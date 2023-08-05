#
#   Hello World server in Python
#   Binds REP socket to tcp://*:5555
#   Expects b"Hello" from client, replies with b"World"
#

import time
import zmq

from .interface import DistributorManagerConfigInterface
from ..common.helpers import get_path_to_file_in_same_folder

class DistributorManager:
    
    def __init__(self, config_file: str=None) -> None:
        self._config = DistributorManager.load_config(config_file=config_file)
        self.spin_up_network_interface()

    @staticmethod
    def load_config(config_file: str=None) -> DistributorManagerConfigInterface:
        return DistributorManagerConfig(
            path_to_config_file=config_file
        )

    


class DistributorManagerConfig(DistributorManagerConfigInterface):

    def __init__(self, path_to_config_file:str=None) -> None:
        super().__init__(
            config_file_path=(
                path_to_config_file if path_to_config_file
                else get_path_to_file_in_same_folder(
                    script__file__=__file__,
                    neighbor_file_name="default.yaml"
                )
            )
        )
    
    @property
    def tcp_address(self) -> str:
        return self._raw_config["network_interface"]["tcp"]["address"]

    @property
    def ipc_address(self) -> str:
        return self._raw_config["network_interface"]["ipc"]["address"]


context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    #  Wait for next request from client
    message = socket.recv()
    print(f"Received request: {message}")

    #  Do some 'work'
    time.sleep(1)

    #  Send reply back to client
    socket.send_string("World")