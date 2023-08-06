#!/usr/bin/env python3

from argparse import ArgumentParser, Namespace

import zmq

def parse_cli_command() -> Namespace:
    parser = ArgumentParser()
    # Log level
    parser.add_argument("-c", "--channel_address", help="Put channel address here", required=True)

    return parser.parse_args()

def test_channel_function(channel_address:str):
    context = zmq.Context()
    print(f"Connecting to server {channel_address}")
    socket:zmq.sugar.Socket = context.socket(zmq.REQ)
    socket.connect(channel_address)
    socket.send_json({
        "Test":1
    })
    rep = socket.recv_json()
    print(f"Server reply: {rep}")


if __name__ == "__main__":
    args = parse_cli_command()
    # Run the DistributorManger
    test_channel_function(channel_address=args.channel_address)