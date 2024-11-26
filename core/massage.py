import logging
import sys
sys.path.append('/opt/xtream-ui_bot/')
from core.vod_handler import check_and_notify_new_vod
from core.series_handler import check_and_notify_new_series
from config.config import API_URL, USERNAME, PASSWORD, TELEGRAM_TOKEN, CHANNELS
from termcolor import colored

logging.basicConfig(level=logging.INFO, format="%(message)s")

def send_to_all_channels_for_vod():
    """
    Sends VOD (Video On Demand) information to all specified Telegram channels.
    """
    try:
        # Notify all channels about new VODs
        check_and_notify_new_vod(API_URL, USERNAME, PASSWORD, TELEGRAM_TOKEN, CHANNELS)
        # Success message
        print(colored("Success: Film data sent to all channels.", 'cyan'))
    except Exception as e:
        # Failure message with error details
        print(colored(f"Failure: Failed to send film data. Error: {str(e)}", 'red'))

def send_to_all_channels_for_series():
    """
    Sends Series information to all specified Telegram channels.
    """
    try:
        # Notify all channels about new Series
        check_and_notify_new_series(API_URL, USERNAME, PASSWORD, TELEGRAM_TOKEN, CHANNELS)
        # Success message
        print(colored("Success: Series data sent to all channels.", 'cyan'))
    except Exception as e:
        # Failure message with error details
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
