import os
import yaml

from typing import Dict



def load_yaml_file(path_to_yaml_file:str) -> Dict:
    """Load and return the content of a yaml file as a dictionary

    Args:
        path_to_yaml_file ([str]): Path to the yaml file

    Returns:
        [Dict]: A dictionary representing the yaml file
    """
    with open(path_to_yaml_file, "r") as yaml_file:
        yaml_file_content_dict = yaml.safe_load(yaml_file)

    return yaml_file_content_dict


def get_path_to_file_in_same_folder(script__file__:str, neighbor_file_name:str) -> str:
    """Return the absoluate path to the file named neighbor_file_name in the same folder with the script whose
    absoluate file path is in script__file__

    Args:
        script__file__ (str): the __file__ of the script
        neighbor_file_name (str): The name of the neighbor file in the folder

    Returns:
        str: Absoluate path to the neighbot_file_name
    """
    # Get current folder of the script
    current_folder = os.path.abspath(os.path.dirname(__file__))
    # Join the folder with the neighbor file name to get absoluate path
    return os.path.join(current_folder, neighbor_file_name)