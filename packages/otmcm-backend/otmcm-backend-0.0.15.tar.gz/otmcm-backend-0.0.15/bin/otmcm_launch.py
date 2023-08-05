#!/usr/bin/env python3

from argparse import ArgumentParser, Namespace

from otmcm_backend.distributor_manager.core import (
    DistributorManager
)


def parse_cli_command() -> Namespace:
    parser = ArgumentParser()
    # Log level
    parser.add_argument("-v", "--verbose", help="Verbose to see all debug message", action="store_false")

    return parser.parse_args()


if __name__ == "__main__":
    args = parse_cli_command()
    # Run the DistributorManger
    DistributorManager(
        log_verbose=args.verbose
    )