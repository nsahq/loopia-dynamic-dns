#!/usr/bin/python3
"""
Config manager for easy and fast configuration functionality

This library is for educational purposes only.
Do no evil, do not break local or internation laws!
By using this code, you take full responisbillity for your actions.
The author have granted code access for educational purposes and is
not liable for any missuse.
"""
__author__ = "Jonas Werme"
__copyright__ = "Copyright (c) 2021 Jonas Werme"
__credits__ = []
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Jonas Werme"
__email__ = "jonas[dot]werme[at]hoofbite[dot]com"
__status__ = "Prototype"

import yaml
import sys


def yaml_config_to_dict(
    config_file: str = "config.yml", expected_keys: list = [], allow_empty: bool = False
) -> dict:
    """
    Read configuration file and return as dict

    Keyword Arguments:
        config_file {str} -- Path to configuration file (default: {'config.yml'})

    Returns:
        dict -- Configuration settings
    """
    try:
        with open(config_file, "r") as file:
            cfg = yaml.safe_load(file)
    except FileNotFoundError:
        print("Missing configuration file: ", config_file)
    except Exception as e:
        raise Exception(f"File error for {config_file}: {e}")


    if expected_keys != []:
        # Validate expected config
        for key in expected_keys:
            missed = []
            if key not in cfg:
                missed.append(key)
            elif cfg[key] in ["", (), [], {}, None] and allow_empty == False:
                raise ValueError(f"Configuration error. Invalid value in: {key}")

    return cfg
