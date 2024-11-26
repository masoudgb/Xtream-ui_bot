import logging
import os
import json
import sys
from termcolor import colored

# Adding the path to sys
sys.path.append('/opt/xtream-ui_bot/')
from core.vod_handler import check_and_notify_new_vod
from core.series_handler import check_and_notify_new_series
from config.config import API_URL, USERNAME, PASSWORD, TELEGRAM_TOKEN, CHANNELS

logging.basicConfig(level=logging.INFO, format="%(message)s")

# Path to the JSON files
JSON_DIR = "json"
VOD_FILE = os.path.join(JSON_DIR, "vod_ids.json")
SERIES_FILE = os.path.join(JSON_DIR, "series_ids.json")

def initialize_json_file(file_path):
    """
    Creates a JSON file if it doesn't exist.
    """
    if not os.path.exists(JSON_DIR):
        os.makedirs(JSON_DIR)  # Create the folder if it doesn't exist
    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            json.dump([], f)  # Save an empty list to the file

def read_json(file_path):
    """
    Reads data from a JSON file.
    """
    with open(file_path, "r") as f:
        return json.load(f)

def write_json(file_path, data):
    """
    Writes data to a JSON file.
    """
    with open(file_path, "w") as f:
        json.dump(data, f)

def send_to_all_channels_for_vod():
    """
    Sends VOD (Video On Demand) information to all specified Telegram channels.
    Only new VOD IDs that are not already sent are processed.
    """
    try:
        # Initialize the JSON file
        initialize_json_file(VOD_FILE)
        
        # Read previously sent VOD IDs
        sent_vod_ids = set(read_json(VOD_FILE))
        
        # Fetch new VOD IDs
        new_vod_ids = check_and_notify_new_vod(API_URL, USERNAME, PASSWORD, TELEGRAM_TOKEN, CHANNELS)
        
        # Identify VOD IDs that are not yet sent
        to_send_vod_ids = [vod_id for vod_id in new_vod_ids if vod_id not in sent_vod_ids]
        
        # Send VODs to channels
        for vod_id in to_send_vod_ids:
            logging.info(f"Sending VOD ID {vod_id}...")
            # Implement Telegram message sending here
        
        # Update the JSON file with new VOD IDs after sending
        sent_vod_ids.update(to_send_vod_ids)
        write_json(VOD_FILE, list(sent_vod_ids))
        
        print(colored("Success: Film data sent to all channels.", 'cyan'))
    except Exception as e:
        print(colored(f"Failure: Failed to send film data. Error: {str(e)}", 'red'))

def send_to_all_channels_for_series():
    """
    Sends Series information to all specified Telegram channels.
    Only new Series IDs that are not already sent are processed.
    """
    try:
        # Initialize the JSON file
        initialize_json_file(SERIES_FILE)
        
        # Read previously sent Series IDs
        sent_series_ids = set(read_json(SERIES_FILE))
        
        # Fetch new Series IDs
        new_series_ids = check_and_notify_new_series(API_URL, USERNAME, PASSWORD, TELEGRAM_TOKEN, CHANNELS)
        
        # Identify Series IDs that are not yet sent
        to_send_series_ids = [series_id for series_id in new_series_ids if series_id not in sent_series_ids]
        
        # Send Series to channels
        for series_id in to_send_series_ids:
            logging.info(f"Sending Series ID {series_id}...")
            # Implement Telegram message sending here
        
        # Update the JSON file with new Series IDs after sending
        sent_series_ids.update(to_send_series_ids)
        write_json(SERIES_FILE, list(sent_series_ids))
        
        print(colored("Success: Series data sent to all channels.", 'cyan'))
    except Exception as e:
        print(colored(f"Failure: Failed to send series data. Error: {str(e)}", 'red'))

if __name__ == "__main__":
    """
    Main execution block:
    - Sends VOD information to all channels.
    - Sends Series information to all channels.
    - Logs and prints operation status.
    """
    # Send VOD information to all channels
    logging.info("Checking and sending new films to channels...")
    send_to_all_channels_for_vod()
    print(colored("Finished sending films to all channels!", 'yellow'))

    # Send Series information to all channels
    logging.info("Checking and sending new series to channels...")
    send_to_all_channels_for_series()
    print(colored("Finished sending series to all channels!", 'yellow'))

    # End of operation
    print(colored("Message sent successfully!", 'green'))
