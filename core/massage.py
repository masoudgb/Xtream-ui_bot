import logging
from core.vod_handler import check_and_notify_new_vod  # Import for handling VOD notifications
from core.series_handler import check_and_notify_new_series  # Import for handling Series notifications
from config.config import API_URL, USERNAME, PASSWORD, TELEGRAM_TOKEN, CHANNELS  # Import required configuration
from termcolor import colored  # For colored console messages

# Configure logging to show only messages (no additional log formatting)
logging.basicConfig(level=logging.INFO, format="%(message)s")

def send_to_all_channels_for_vod():
    """
    Send VOD (Video On Demand) information to all specified channels.
    """
    try:
        # Trigger notification for VOD
        check_and_notify_new_vod(API_URL, USERNAME, PASSWORD, TELEGRAM_TOKEN, CHANNELS)
        # Success log
        print(colored("Success: Film data sent to all channels.", 'cyan'))
    except Exception as e:
        # Failure log with error details
        print(colored(f"Failure: Failed to send film data. Error: {str(e)}", 'red'))

def send_to_all_channels_for_series():
    """
    Send Series information to all specified channels.
    """
    try:
        # Trigger notification for Series
        check_and_notify_new_series(API_URL, USERNAME, PASSWORD, TELEGRAM_TOKEN, CHANNELS)
        # Success log
        print(colored("Success: Series data sent to all channels.", 'cyan'))
    except Exception as e:
        # Failure log with error details
        print(colored(f"Failure: Failed to send series data. Error: {str(e)}", 'red'))

if __name__ == "__main__":
    """
    Main execution block to handle sending VOD and Series notifications to Telegram channels.
    """
    # Send VOD information
    logging.info("Checking and sending new films to channels...")
    send_to_all_channels_for_vod()
    print(colored("Finished sending films to all channels!", 'yellow'))

    # Send Series information
    logging.info("Checking and sending new series to channels...")
    send_to_all_channels_for_series()
    print(colored("Finished sending series to all channels!", 'yellow'))

    # Operation complete
    print(colored("Message sent successfully!", 'green'))
