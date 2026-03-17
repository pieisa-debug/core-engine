import logging
import os
import uuid
from datetime import datetime
from typing import List

from core_engine.errors import CoreEngineError
from core_engine.exceptions import CoreEngineException

class Utils:
    @staticmethod
    def generate_id(length: int = 32) -> str:
        return str(uuid.uuid4().int)[:length]

    @staticmethod
    def get_current_datetime() -> datetime:
        return datetime.now()

    @staticmethod
    def get_log_level(level: int) -> str:
        levels = {
            10: "DEBUG",
            20: "INFO",
            30: "WARNING",
            40: "ERROR",
            50: "CRITICAL"
        }
        if level not in levels:
            raise CoreEngineError(f"Unknown log level: {level}")
        return levels[level]

    @staticmethod
    def get_directory_path(directory: str) -> str:
        return os.path.abspath(os.path.expanduser(os.path.expandvars(directory)))

    @staticmethod
    def get_file_path(directory: str, filename: str) -> str:
        return os.path.join(Utils.get_directory_path(directory), filename)

    @staticmethod
    def get_file_extension(filename: str) -> str:
        return os.path.splitext(filename)[1]

    @staticmethod
    def is_valid_file(file_path: str) -> bool:
        return os.path.exists(file_path) and os.path.isfile(file_path)

    @staticmethod
    def is_valid_directory(directory: str) -> bool:
        return os.path.exists(directory) and os.path.isdir(directory)

    @staticmethod
    def get_file_size(file_path: str) -> int:
        return os.path.getsize(file_path)

    @staticmethod
    def get_file_last_modified(file_path: str) -> datetime:
        return datetime.fromtimestamp(os.path.getmtime(file_path))

    @staticmethod
    def check_file_exists(file_path: str) -> bool:
        return os.path.exists(file_path)

    @staticmethod
    def check_directory_exists(directory: str) -> bool:
        return os.path.exists(directory)

    @staticmethod
    def get_parent_directory(file_path: str) -> str:
        return os.path.dirname(file_path)

    @staticmethod
    def get_child_directories(directory: str) -> List[str]:
        return [name for name in os.listdir(directory) if os.path.isdir(os.path.join(directory, name))]

    @staticmethod
    def get_child_files(directory: str) -> List[str]:
        return [name for name in os.listdir(directory) if os.path.isfile(os.path.join(directory, name))]

    @staticmethod
    def get_log_filename(directory: str, filename: str, log_level: int) -> str:
        log_filename = f"{Utils.get_log_level(log_level)}_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
        return Utils.get_file_path(directory, log_filename)

    @staticmethod
    def configure_logging(directory: str, log_level: int) -> None:
        log_filename = Utils.get_log_filename(directory, "core_engine.log", log_level)
        logging.basicConfig(
            format="%(asctime)s %(levelname)s: %(message)s",
            level=getattr(logging, Utils.get_log_level(log_level).upper()),
            handlers=[logging.FileHandler(log_filename)]
        )