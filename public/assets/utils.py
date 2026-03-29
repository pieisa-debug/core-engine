# utils.py

import os
import re
import logging
from typing import List, Dict, Optional

def get_current_directory() -> str:
    return os.path.dirname(os.path.abspath(__file__))

def get_parent_directory() -> str:
    return os.path.dirname(get_current_directory())

def get_config_path() -> str:
    return os.path.join(get_parent_directory(), 'config.json')

def load_config() -> Dict[str, str]:
    try:
        with open(get_config_path(), 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        logging.error(f"Config file not found: {get_config_path()}")
        return {}

def get_user_data_path() -> str:
    return os.path.join(get_parent_directory(), 'user_data')

def create_user_data_directory() -> None:
    if not os.path.exists(get_user_data_path()):
        os.makedirs(get_user_data_path())

def validate_email(email: str) -> bool:
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(pattern, email))

def validate_password(password: str) -> bool:
    return len(password) >= 8

def get_system_architecture() -> str:
    return os.uname().machine