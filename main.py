# 1. Import Dependencies
import os
import sys
import subprocess
import logging
from termcolor import colored
from dotenv import load_dotenv
from core.vod_handler import check_and_notify_new_vod
from core.series_handler import check_and_notify_new_series

# Install/upgrade pip and dependencies
def install_or_update_dependencies():
    try:
        print(colored("Checking and upgrading pip...", "green"))
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip'])
        print(colored("Pip upgraded successfully.", "cyan"))

        print(colored("Installing required packages from requirements.txt...", "green"))
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
        print(colored("Dependencies installed successfully.", "cyan"))
    except Exception as e:
        print(colored(f"Error installing dependencies: {e}", "red"))
        sys.exit(1)

# Install dependencies on script start
install_or_update_dependencies()

# 2. Load Configuration
load_dotenv()

API_URL = os.getenv("API_URL")
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
DEFAULT_VOD_COVER_URL = os.getenv("DEFAULT_VOD_COVER_URL")
DEFAULT_SERIES_COVER_URL = os.getenv("DEFAULT_SERIES_COVER_URL")

# Parse channels
CHANNELS = []
channel_index = 1
while True:
    channel_id = os.getenv(f"CHANNEL_{channel_index}_ID")
    channel_link = os.getenv(f"CHANNEL_{channel_index}_LINK")
    if not channel_id or not channel_link:
        break
    CHANNELS.append({"id": channel_id, "link": channel_link})
    channel_index += 1

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(message)s")

# 3. Notification Functions
# Sends VOD data to all channels
def send_to_all_channels_for_vod():
    try:
        check_and_notify_new_vod(API_URL, USERNAME, PASSWORD, TELEGRAM_TOKEN, CHANNELS, DEFAULT_VOD_COVER_URL)
        print(colored("VOD notifications sent successfully.", "cyan"))
    except Exception as e:
        print(colored(f"Error sending VOD notifications: {str(e)}", "red"))

# Sends Series data to all channels
def send_to_all_channels_for_series():
    try:
        check_and_notify_new_series(API_URL, USERNAME, PASSWORD, TELEGRAM_TOKEN, CHANNELS, DEFAULT_SERIES_COVER_URL)
        print(colored("Series notifications sent successfully.", "cyan"))
    except Exception as e:
        print(colored(f"Error sending Series notifications: {str(e)}", "red"))
        
# 4. Installation Process
def install_script():
    print(colored("Starting installation...", "green"))

    # Gather user input
    api_url = input(colored("Enter the API server URL (e.g., http://example.com:8080): ", "green"))
    username = input(colored("Enter the API username: ", "green"))
    password = input(colored("Enter the API password: ", "green"))
    telegram_token = input(colored("Enter the Telegram bot token: ", "green"))
    default_vod_cover_url = input(colored("Enter the default film cover URL: ", "green"))
    default_series_cover_url = input(colored("Enter the default series cover URL: ", "green"))

    # Gather channels
    channels = []
    while True:
        channel_id = input(colored("Enter a Telegram channel ID (or press Enter to finish): ", "green"))
        if not channel_id:
            break
        channel_link = input(colored("Enter the channel link: ", "green"))
        channels.append({"id": channel_id, "link": channel_link})

    # Write to .env file
    with open(".env", "w") as env_file:
        env_file.write(f"API_URL={api_url}\n")
        env_file.write(f"USERNAME={username}\n")
        env_file.write(f"PASSWORD={password}\n")
        env_file.write(f"TELEGRAM_TOKEN={telegram_token}\n")
        env_file.write(f"DEFAULT_VOD_COVER_URL={default_vod_cover_url}\n")
        env_file.write(f"DEFAULT_SERIES_COVER_URL={default_series_cover_url}\n")
        for index, channel in enumerate(channels, start=1):
            env_file.write(f"CHANNEL_{index}_ID={channel['id']}\n")
            env_file.write(f"CHANNEL_{index}_LINK={channel['link']}\n")

    print(colored("Installation completed successfully!", "cyan"))
    
# 5. Main Menu
def display_main_menu():
    while True:
        print(colored("\nMain Menu:", "green"))
        print(colored("1. Install Script", "green"))
        print(colored("2. Manage Script", "green"))
        print(colored("3. Remove Script", "green"))
        print(colored("4. Update Script", "green"))
        print(colored("5. Exit", "green"))

        choice = input(colored("Enter your choice: ", "green"))

        if choice == "1":
            install_script()
        elif choice == "2":
            manage_script()
        elif choice == "3":
            remove_script()
        elif choice == "4":
            update_script()
        elif choice == "5":
            print(colored("Exiting the script. Goodbye!", "green"))
            sys.exit(0)
        else:
            print(colored("Invalid choice. Please try again.", "red"))
            
# 6. Manage Script
def manage_script():
    print(colored("Manage Script (Functionality to be implemented)", "blue"))

# 7. Remove Script
def remove_script():
    print(colored("Removing Script (Functionality to be implemented)", "blue"))

# 8. Update Script
def update_script():
    print(colored("Updating Script (Functionality to be implemented)", "blue"))
    
# 6. Manage Script
def manage_script():
    print(colored("Manage Script (Functionality to be implemented)", "blue"))

# 7. Remove Script
def remove_script():
    print(colored("Removing Script (Functionality to be implemented)", "blue"))

# 8. Update Script
def update_script():
    print(colored("Updating Script (Functionality to be implemented)", "blue"))
    
# 9. Main Execution Block
if __name__ == "__main__":
    """
    Main execution block.
    """
    display_main_menu()
