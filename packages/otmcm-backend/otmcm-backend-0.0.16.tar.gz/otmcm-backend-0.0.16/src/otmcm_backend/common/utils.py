import yaml

from .helpers import load_yaml_file

class ConfigObject():

    def __init__(self, config_file_path) -> None:
        self._raw_config = load_yaml_file(path_to_yaml_file=config_file_path)
