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
        print(colored("5. Manage Channels", "green"))
        print(colored("6. Exit", "green"))

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
            manage_channels_menu()  # Call a separate menu for channel management
        elif choice == "6":
            print(colored("Exiting the script. Goodbye!", "green"))
            sys.exit(0)
        else:
            print(colored("Invalid choice. Please try again.", "red"))

# Channel Management Menu
def manage_channels_menu():
    """Menu for managing channels."""
    while True:
        print("\n" + "=" * 30)
        print(colored("Channel Management", "blue"))
        print("=" * 30)
        print("1. Add a New Channel")
        print("2. Stop Sending to a Channel")
        print("3. Reactivate a Stopped Channel")
        print("4. Delete a Channel")
        print("5. Back to Main Menu")
        print("=" * 30)

        choice = input("Enter your choice: ")

        if choice == "1":
            add_new_channel()
        elif choice == "2":
            stop_channel()
        elif choice == "3":
            reactivate_channel()
        elif choice == "4":
            delete_channel()
        elif choice == "5":
            print(colored("Returning to main menu...", 'yellow'))
            break
        else:
            print(colored("Invalid choice. Please try again.", 'red'))

# Add New Channel
def add_new_channel():
    """Add a new channel to the .env file."""
    env_data = load_env_file()
    channel_count = len([key for key in env_data if key.startswith("CHANNEL_") and key.endswith("_ID")])

    while True:
        channel_id = input("Enter the new channel ID: ").strip()
        channel_link = input("Enter the new channel link: ").strip()

        env_data[f"CHANNEL_{channel_count + 1}_ID"] = channel_id
        env_data[f"CHANNEL_{channel_count + 1}_LINK"] = channel_link
        channel_count += 1

        save_env_file(env_data)
        print(colored("Channel added successfully!", 'green'))

        more_channels = input("Do you want to add another channel? (y/n): ").strip().lower()
        if more_channels != "y":
            break

# Stop Channel
def stop_channel():
    """Stop sending to a channel by commenting it out in the .env file."""
    env_data = load_env_file()
    channel_ids = {i + 1: key for i, key in enumerate(env_data) if key.startswith("CHANNEL_") and key.endswith("_ID")}

    print("\nList of Channels:")
    for index, channel_id in channel_ids.items():
        print(f"{index}. {env_data[channel_id]}")

    while True:
        choice = int(input("\nEnter the number of the channel to stop: "))
        if choice in channel_ids:
            channel_id_key = channel_ids[choice]
            channel_link_key = channel_id_key.replace("_ID", "_LINK")

            env_data[channel_id_key] = f"#{env_data[channel_id_key]}"
            env_data[channel_link_key] = f"#{env_data[channel_link_key]}"

            save_env_file(env_data)
            print(colored("Channel stopped successfully!", 'green'))
        else:
            print(colored("Invalid choice. Please try again.", 'red'))

        more_channels = input("Do you want to stop another channel? (y/n): ").strip().lower()
        if more_channels != "y":
            break

# Reactivate Channel
def reactivate_channel():
    """Reactivate a stopped channel by uncommenting it in the .env file."""
    env_data = load_env_file()
    stopped_channels = {i + 1: key for i, key in enumerate(env_data) if key.startswith("#CHANNEL_") and key.endswith("_ID")}

    print("\nList of Stopped Channels:")
    for index, channel_id in stopped_channels.items():
        print(f"{index}. {env_data[channel_id]}")

    while True:
        choice = int(input("\nEnter the number of the channel to reactivate: "))
        if choice in stopped_channels:
            channel_id_key = stopped_channels[choice]
            channel_link_key = channel_id_key.replace("_ID", "_LINK")

            env_data[channel_id_key] = env_data[channel_id_key][1:]  # Remove "#"
            env_data[channel_link_key] = env_data[channel_link_key][1:]  # Remove "#"

            save_env_file(env_data)
            print(colored("Channel reactivated successfully!", 'green'))
        else:
            print(colored("Invalid choice. Please try again.", 'red'))

        more_channels = input("Do you want to reactivate another channel? (y/n): ").strip().lower()
        if more_channels != "y":
            break

# Delete Channel
def delete_channel():
    """Delete a channel from the .env file."""
    env_data = load_env_file()
    channel_ids = {i + 1: key for i, key in enumerate(env_data) if key.startswith("CHANNEL_") and key.endswith("_ID")}

    print("\nList of Channels:")
    for index, channel_id in channel_ids.items():
        print(f"{index}. {env_data[channel_id]}")

    while True:
        choice = int(input("\nEnter the number of the channel to delete: "))
        if choice in channel_ids:
            channel_id_key = channel_ids[choice]
            channel_link_key = channel_id_key.replace("_ID", "_LINK")

            del env_data[channel_id_key]
            del env_data[channel_link_key]

            save_env_file(env_data)
            print(colored("Channel deleted successfully!", 'green'))
        else:
            print(colored("Invalid choice. Please try again.", 'red'))

        more_channels = input("Do you want to delete another channel? (y/n): ").strip().lower()
        if more_channels != "y":
            break
            
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
