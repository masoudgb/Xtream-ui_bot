import os
import sys
import time
import shutil
import subprocess
from colorama import Fore, Style, init

init(autoreset=True)

def check_root():
    """
    Verify if the script is executed with root privileges.
    """
    if os.geteuid() != 0:
        print(Fore.RED + "Error: You need to run this script as root!")
        exit(1)

# Install prerequisites
def install_prerequisites():
    """
    Update the server and install required packages and libraries.
    """
    print(Fore.CYAN + "Updating server and installing prerequisites...")

    try:
        # Update the package list
        print(Fore.YELLOW + "Updating package list...")
        subprocess.run(["apt", "update", "-y"], check=True)

        # Install Python3 and pip
        print(Fore.YELLOW + "Installing Python3 and pip...")
        subprocess.run(["apt", "install", "python3-pip", "-y"], check=True)

        # Install required Python libraries
        print(Fore.YELLOW + "Installing required Python libraries...")
        required_libraries = [
            "python-telegram-bot",
            "termcolor",
            "python-dotenv",
            "requests"
        ]
        for lib in required_libraries:
            print(Fore.YELLOW + f"Installing {lib}...")
            subprocess.run(["pip3", "install", lib], check=True)

        print(Fore.GREEN + "All prerequisites have been successfully installed.")
    except subprocess.CalledProcessError as e:
        print(Fore.RED + f"Error installing prerequisites: {str(e)}")
        exit(1)

# Move project to /opt
def setup_project_in_opt():
    """
    Ensure the project is located in /opt and navigate to the correct directory.
    """
    current_path = os.getcwd()  # Get the current working directory
    target_path = "/opt/xtream-ui_bot"

    if current_path != target_path:
        try:
            # Check if the /opt directory already contains the project
            if not os.path.exists(target_path):
                print(Fore.YELLOW + "Moving project files to /opt...")
                shutil.move(current_path, target_path)  # Move the project to /opt
            # Change the current directory to /opt/xtream-ui_bot
            os.chdir(target_path)
            print(Fore.GREEN + f"Successfully moved to and set up in {target_path}.")
        except Exception as e:
            print(Fore.RED + f"Error moving project to /opt: {str(e)}")
            exit(1)
    else:
        print(Fore.GREEN + f"Project is already located in {target_path}.")

# Installation process
def install_bot():
    """
    Handles the installation process of xtream-ui bot.
    """
    print(Fore.GREEN + "Installing xtream-ui bot...")

    # Check for root privileges
    check_root()

    # Install prerequisites
    install_prerequisites()

    # Move the project to /opt
    setup_project_in_opt()

    # Prompt the user for environment variables
    print(Fore.WHITE + "Please enter the following information:")

    # API Information
    api_url = input(Fore.WHITE + "Enter the API URL (e.g., http://myserver.com:8080): ")
    username = input(Fore.WHITE + "Enter the Username: ")
    password = input(Fore.WHITE + "Enter the Password: ")

    # Telegram Information
    telegram_token = input(Fore.WHITE + "Enter Your Telegram Bot Token: ")

    # Default Cover URLs
    default_vod_cover_url = input(Fore.WHITE + "Default VOD Cover URL: ")
    default_series_cover_url = input(Fore.WHITE + "Default Series Cover URL: ")

    # Channels Information
    channel_1_id = input(Fore.WHITE + "Enter Channel ID (e.g., @mychannel): ")
    channel_1_link = input(Fore.WHITE + "Enter the Channel Link (e.g., https://t.me/mychannel): ")

    # Create or write the .env file
    env_path = os.path.join(os.getcwd(), '.env')
    with open(env_path, 'w') as env_file:
        env_file.write(f"# API Information\n")
        env_file.write(f"API_URL={api_url}/player_api.php\n")
        env_file.write(f"USERNAME={username}\n")
        env_file.write(f"PASSWORD={password}\n\n")
        
        env_file.write(f"# Telegram Information\n")
        env_file.write(f"TELEGRAM_TOKEN={telegram_token}\n\n")
        
        env_file.write(f"# Default Cover URLs\n")
        env_file.write(f"DEFAULT_VOD_COVER_URL={default_vod_cover_url}\n")
        env_file.write(f"DEFAULT_SERIES_COVER_URL={default_series_cover_url}\n\n")
        
        env_file.write(f"# Channels Information\n")
        env_file.write(f"CHANNEL_1_ID={channel_1_id}\n")
        env_file.write(f"CHANNEL_1_LINK={channel_1_link}\n")

    print(Fore.GREEN + "Installation completed successfully.")
    print(Fore.YELLOW + "To send a message, refer to the sending schedule section in Manage xtream-ui bot/Manage Post Timing")
    
    # Return to the main menu after installation
    main() 

def animated_text_with_border(text, delay=0.05):
    text_length = len(text)
    border_line = "═" * (text_length + 2)
    
    print(Fore.WHITE + "╔" + border_line + "╗")
    print(Fore.WHITE + "║", end=" ")

    for char in text:
        sys.stdout.write(Fore.LIGHTCYAN_EX + char)
        sys.stdout.flush()
        time.sleep(delay)
    
    print(Fore.WHITE + " ║")
    print(Fore.WHITE + "╚" + border_line + "╝")
    
    print(Style.RESET_ALL)

# Main menu
def main():
    """
    Main menu for the bot setup and management.
    """
    animated_text_with_border("xtream-ui bot powered by masoud_gb")
    # Display options with green text and white numbers
    print(Fore.WHITE + "1." + Fore.GREEN + " Install xtream-ui bot")
    print(Fore.WHITE + "2." + Fore.GREEN + " Manage xtream-ui bot")
    print(Fore.WHITE + "3." + Fore.GREEN + " Update xtream-ui bot")
    print(Fore.WHITE + "4." + Fore.GREEN + " Uninstall")
    print(Fore.WHITE + "5." + Fore.GREEN + " Exit")
    print(Style.RESET_ALL)
    
    # Get user input
    choice = input(Fore.WHITE + "Please choose an option: ")
    
    if choice == "1":
        install_bot()
    elif choice == "2":
        manage_bot()
    elif choice == "3":
        update_bot()
    elif choice == "4":
        uninstall_bot()
    elif choice == "5":
        exit_program()
    else:
        print(Fore.RED + "Invalid option, please try again.")
        main()
        
# Magageing bot
def manage_bot():
    print(Fore.GREEN + "Managing xtream-ui bot...")

def manage_bot():
    print(Fore.WHITE + "Manage xtream-ui bot:")
    print(Fore.WHITE + "1." + Fore.GREEN + " Manage Channels")
    print(Fore.WHITE + "2." + Fore.GREEN + " Manage Post Timing")
    print(Fore.WHITE + "3." + Fore.GREEN + " Back")

    choice = input(Fore.WHITE + "Choose an option: ")

    if choice == "1":
        manage_channels()
    elif choice == "2":
        manage_post_timing()
    elif choice == "3":
        print(Fore.WHITE + "Returning to the previous menu.")
        main()
    else:
        print(Fore.RED + "Invalid option, returning to main menu.")
        main()

# Channel management
def manage_channels():
    print(Fore.GREEN + "Manage Channels:")
    print(Fore.WHITE + "1." + Fore.GREEN + " Add Channel")
    print(Fore.WHITE + "2." + Fore.GREEN + " Stop Sending to Channel")
    print(Fore.WHITE + "3." + Fore.GREEN + " Resume Sending to Channel")
    print(Fore.WHITE + "4." + Fore.GREEN + " Remove Channel")
    print(Fore.WHITE + "5." + Fore.GREEN + " Back")

    choice = input(Fore.WHITE + "Please Choose an option: ")

    if choice == "1":
        add_channel()
    elif choice == "2":
        stop_channel()
    elif choice == "3":
        resume_channel()
    elif choice == "4":
        remove_channel()
    elif choice == "5":
        print(Fore.WHITE + "Returning to the previous menu.")
        manage_bot() 
    else:
        print(Fore.RED + "Invalid option, returning to manage menu.")
        manage_bot()

# Path to the .env file
ENV_FILE_PATH = '/opt/xtream-ui_bot/.env'

# 1.1 Add Channel
def add_channel():
    """
    Adds a new channel to the .env file. Checks if the channel ID is already present
    to avoid duplicates.
    """
    # Read current channel index from the .env file
    channel_index = 1
    existing_channels = set()  # To track existing channel IDs
    
    try:
        with open(ENV_FILE_PATH, 'r') as env_file:
            for line in env_file:
                if line.startswith("CHANNEL_") and "_ID=" in line:
                    # Extract the existing channel ID and add it to the set
                    existing_channels.add(line.split('=')[1].strip())
                    channel_index += 1
    except FileNotFoundError:
        print(Fore.YELLOW + ".env file not found. It will be created.")
    
    # Get channel information from the user
    channel_id = input(Fore.WHITE + "Enter Channel ID (e.g., @mychannel): ").strip()
    
    # Check if the channel ID is already in the .env file
    if channel_id in existing_channels:
        print(Fore.YELLOW + "Channel ID already exists.")
        return  # Stop further processing
    
    channel_link = input(Fore.WHITE + "Enter Channel Link (e.g., https://t.me/mychannel): ").strip()
    
    # Append channel information to the .env file
    os.makedirs(os.path.dirname(ENV_FILE_PATH), exist_ok=True)  # Ensure directories exist
    with open(ENV_FILE_PATH, 'a') as env_file:
        env_file.write(f"CHANNEL_{channel_index}_ID={channel_id}\n")
        env_file.write(f"CHANNEL_{channel_index}_LINK={channel_link}\n")
    
    print(Fore.GREEN + f"Channel added successfully as CHANNEL_{channel_index}.")
    manage_channels()

# 1.2 Stop sending to a channel
def stop_channel():
    """
    Stops sending messages to a specified channel.
    """
    modify_channel_status("stop")

# 1.3 Resume sending to a channel
def resume_channel():
    """
    Resumes sending messages to a specified channel.
    """
    modify_channel_status("resume")

# 1.4 Remove a channel
def remove_channel():
    """
    Removes a channel from the .env file.
    """
    modify_channel_status("remove")

# Modify channel status (stop, resume, or remove)
def modify_channel_status(action):
    """
    Modifies the status of a channel (stop, resume, or remove).
    
    Parameters:
    action (str): The action to perform on the channel (e.g., "stop", "resume", "remove").
    """
    channels = {}
    try:
        with open(ENV_FILE_PATH, 'r') as env_file:
            lines = env_file.readlines()
    except FileNotFoundError:
        print(Fore.RED + ".env file not found.")
        return
    
    # Collect channels from the .env file
    for line in lines:
        if line.startswith("CHANNEL_") and "_ID" in line:
            key = line.split('=')[0]
            channel_id = line.split('=')[1].strip()
            channels[key] = channel_id
    
    # Display available channels
    if not channels:
        print(Fore.RED + "No channels found.")
        return
    
    print(Fore.GREEN + "Available Channels:")
    for idx, (key, channel_id) in enumerate(channels.items(), start=1):
        print(Fore.WHITE + f"{idx}." + Fore.GREEN + f" {channel_id}")
    
    try:
        choice = int(input(Fore.WHITE + "Select a channel by number: "))
        selected_key = list(channels.keys())[choice - 1]
    except (IndexError, ValueError):
        print(Fore.RED + "Invalid choice.")
        return
    
    # Edit channels based on the selected action
    with open(ENV_FILE_PATH, 'w') as env_file:
        for line in lines:
            if action == "remove" and selected_key in line:
                continue
            elif action == "stop" and selected_key in line and "_LINK" not in line:
                env_file.write(f"{selected_key}={channels[selected_key]}_STOP\n")
            elif action == "resume" and selected_key in line and "_STOP" in line:
                env_file.write(line.replace("_STOP", ""))
            else:
                env_file.write(line)
    
    print(Fore.GREEN + f"Channel {action} operation completed.")
    manage_channels()

# Post timing management
def manage_post_timing():
    """
    Manages post timing by creating a cron job instead of systemd service and timer files.
    Restarts the cron service after the new cron job is added.
    """
    # Get timing configuration from the user
    interval = input(Fore.WHITE + "Enter post interval in minutes (e.g., 30): ").strip()
    if not interval.isdigit() or int(interval) <= 0:
        print(Fore.RED + "Invalid interval. Please enter a positive number.")
        return
    
    interval = int(interval)
    start_time = input(Fore.WHITE + "Enter start time (HH:mm, default is 08:00): ").strip() or "08:00"
    end_time = input(Fore.WHITE + "Enter end time (HH:mm, default is 23:59): ").strip() or "23:59"
    
    # Validate start and end times
    try:
        start_hour, start_minute = map(int, start_time.split(":"))
        end_hour, end_minute = map(int, end_time.split(":"))
        if not (0 <= start_hour < 24 and 0 <= start_minute < 60 and 0 <= end_hour < 24 and 0 <= end_minute < 60):
            raise ValueError
    except ValueError:
        print(Fore.RED + "Invalid time format. Please enter times in HH:mm format.")
        return

    # Create cron expression
    cron_jobs = []
    for hour in range(start_hour, end_hour + 1):
        if hour == start_hour:
            # First hour: Start from the specified minute
            cron_jobs.append(f"{start_minute}/{interval} {hour} * * * /usr/bin/python3 /opt/xtream-ui_bot/core/massage.py")
        elif hour == end_hour:
            # Last hour: Stop at the specified minute
            cron_jobs.append(f"0/{interval} {hour} * * * /usr/bin/python3 /opt/xtream-ui_bot/core/massage.py")
        else:
            # Full hours in between
            cron_jobs.append(f"0/{interval} {hour} * * * /usr/bin/python3 /opt/xtream-ui_bot/core/massage.py")
    
    # Add the cron job(s) to the crontab
    cron_job_content = "\n".join(cron_jobs)
    with open("/tmp/xtream-ui_bot_cron", "w") as cron_file:
        cron_file.write(cron_job_content + "\n")
    
    os.system("crontab /tmp/xtream-ui_bot_cron")
    os.remove("/tmp/xtream-ui_bot_cron")  # Cleanup temporary file
    
    # Restart cron service
    os.system("systemctl restart cron")
    
    print(Fore.GREEN + "Cron job created and cron service restarted successfully.")
    manage_bot()
    main()

# Update script
def update_bot():
    install_path = "/opt/xtream-ui_bot"  # Path where the bot is installed

    try:
        print(Fore.GREEN + "Updating xtream-ui bot...")

        # Ensure the install path exists
        if not os.path.exists(install_path):
            print(Fore.RED + f"Error: Installation path '{install_path}' does not exist.")
            return

        # Change to the installation directory
        os.chdir(install_path)

        # Check if the directory is a git repository
        if not os.path.exists(".git"):
            print(Fore.YELLOW + "This is not a Git repository. Re-initializing the repository...")
            subprocess.run(['git', 'init'], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            subprocess.run(['git', 'remote', 'add', 'origin', 'https://github.com/masoudgb/Xtream-ui_bot.git'], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            subprocess.run(['git', 'fetch'], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        # Back up the .env file
        if os.path.exists('.env'):
            print(Fore.YELLOW + "Backing up the .env file...")
            os.rename('.env', '.env_backup')

        # Pull the latest changes from GitHub
        print(Fore.YELLOW + "Pulling the latest files from GitHub...")
        subprocess.run(['git', 'pull', 'origin', 'main', '--force'], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        # Restore the .env file
        if os.path.exists('.env_backup'):
            print(Fore.YELLOW + "Restoring the .env file...")
            os.rename('.env_backup', '.env')

        print(Fore.GREEN + "Update completed successfully.")
    except Exception as e:
        print(Fore.RED + f"Error during update: {str(e)}")
        # Restore .env if backup exists
        if os.path.exists('.env_backup'):
            os.rename('.env_backup', '.env')
    main()

# Uninstall
def uninstall_bot():
    """
    Uninstalls the xtream-ui bot, including removing its cron jobs, files, and directories.
    """
    # Confirm uninstallation
    confirmation = input(Fore.RED + "Are you sure you want to uninstall xtream-ui bot? (y/n): ").strip().lower()
    if confirmation != "y":
        print(Fore.YELLOW + "Uninstallation cancelled.")
        main()
        return  # Exit the uninstall function

    try:
        print(Fore.RED + "Uninstalling xtream-ui bot...")

        # Remove cron jobs related to xtream-ui_bot
        print(Fore.YELLOW + "Removing cron jobs for xtream-ui_bot...")
        # Read existing crontab
        current_crontab = subprocess.run(['crontab', '-l'], stdout=subprocess.PIPE, text=True, check=False).stdout
        # Filter out lines related to xtream-ui_bot
        updated_crontab = "\n".join(
            [line for line in current_crontab.splitlines() if "/opt/xtream-ui_bot/core/massage.py" not in line]
        )
        # Update crontab
        with open("/tmp/xtream-ui_bot_cron_uninstall", "w") as cron_file:
            cron_file.write(updated_crontab + "\n")
        subprocess.run(['crontab', '/tmp/xtream-ui_bot_cron_uninstall'], check=False)
        os.remove("/tmp/xtream-ui_bot_cron_uninstall")  # Cleanup temporary file

        # Remove the bot directory
        bot_directory = "/opt/xtream-ui_bot"
        print(Fore.YELLOW + f"Removing bot files from {bot_directory}...")
        if os.path.exists(bot_directory):
            shutil.rmtree(bot_directory)

        # Remove the .env file and its backup if they exist in /opt/xtream-ui_bot
        env_file = os.path.join(bot_directory, ".env")
        env_backup_file = os.path.join(bot_directory, ".env_backup")
        print(Fore.YELLOW + "Removing .env file and backups...")
        if os.path.exists(env_file):
            os.remove(env_file)
        if os.path.exists(env_backup_file):
            os.remove(env_backup_file)

        print(Fore.GREEN + "Uninstallation completed successfully.")
    except Exception as e:
        print(Fore.RED + f"Error during uninstallation: {str(e)}")

    main()
# Exit
def exit_program():
    print(Fore.GREEN + "Exiting...")
    exit()

if __name__ == "__main__":
    main()
