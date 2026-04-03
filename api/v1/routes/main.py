import os
import argparse
import logging
import json
import time
from typing import Dict, Any, Optional

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants
DEFAULT_CONFIG_PATH = 'config.json'
DEFAULT_OUTPUT_PATH = 'output.json'

class CoreEngine:
    """
    Core engine class responsible for processing data based on configuration.
    """

    def __init__(self, config_path: str):
        """
        Initializes the CoreEngine with a configuration file path.

        Args:
            config_path: Path to the configuration file (JSON).
        """
        self.config_path = config_path
        self.config: Dict[str, Any] = self._load_config()

    def _load_config(self) -> Dict[str, Any]:
        """
        Loads the configuration from the specified JSON file.

        Returns:
            A dictionary representing the configuration.

        Raises:
            FileNotFoundError: If the configuration file does not exist.
            json.JSONDecodeError: If the configuration file is not valid JSON.
        """
        try:
            with open(self.config_path, 'r') as f:
                config = json.load(f)
            logging.info(f"Configuration loaded from {self.config_path}")
            return config
        except FileNotFoundError:
            logging.error(f"Configuration file not found: {self.config_path}")
            raise
        except json.JSONDecodeError as e:
            logging.error(f"Invalid JSON in configuration file: {self.config_path} - {e}")
            raise

    def process_data(self, input_data: Any) -> Optional[Dict[str, Any]]:
        """
        Processes the input data according to the configuration.

        Args:
            input_data: The data to be processed.  The type depends on the configuration.

        Returns:
            The processed data as a dictionary, or None if processing fails.
        """
        try:
            # Simulate data processing based on config
            processing_delay = self.config.get('processing_delay', 0)
            time.sleep(processing_delay)

            # Placeholder for actual processing logic
            processed_data = {
                'input': input_data,
                'result': f"Processed with delay: {processing_delay}",
                'config_value': self.config.get('some_config_value', 'default_value')
            }

            logging.info("Data processing completed successfully.")
            return processed_data
        except Exception as e:
            logging.exception("Error during data processing:")
            return None

    def save_output(self, output_data: Dict[str, Any], output_path: str):
        """
        Saves the output data to a JSON file.

        Args:
            output_data: The data to be saved.
            output_path: The path to the output file.
        """
        try:
            with open(output_path, 'w') as f:
                json.dump(output_data, f, indent=4)
            logging.info(f"Output saved to {output_path}")
        except Exception as e:
            logging.error(f"Error saving output to {output_path}: {e}")

def main():
    """
    Main function to execute the core engine.
    """
    parser = argparse.ArgumentParser(description="Core Engine for Data Processing")
    parser.add_argument("--config", type=str, default=DEFAULT_CONFIG_PATH, help="Path to the configuration file.")
    parser.add_argument("--output", type=str, default=DEFAULT_OUTPUT_PATH, help="Path to the output file.")
    args = parser.parse_args()

    try:
        engine = CoreEngine(args.config)
        input_data = {'message': 'Hello, World!'} # Example input
        processed_data = engine.process_data(input_data)

        if processed_data:
            engine.save_output(processed_data, args.output)
        else:
            logging.error("Data processing failed. No output saved.")

    except Exception as e:
        logging.critical(f"An unhandled error occurred: {e}")

if __name__ == "__main__":
    main()