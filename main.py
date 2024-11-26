import os
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

from colorama import Fore, Style
import sys
import time

def gradient_text(text):
    colors = [Fore.LIGHTCYAN_EX, Fore.LIGHTBLUE_EX, Fore.LIGHTGREEN_EX]
    for i, char in enumerate(text):
        sys.stdout.write(colors[i % len(colors)] + char)
        sys.stdout.flush()
        time.sleep(0.03)
    print(Style.RESET_ALL)

gradient_text("xtream-ui bot powered by masoud_gb")

# Main menu
def main():
    """
    Main menu for the bot setup and management.
    """
    #print_ascii_banner()
    print("\n" * 1)
    
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

# 1.1 Add Channel
def add_channel():
    # Read current channel index from the .env file
    channel_index = 1
    try:
        with open('.env', 'r') as env_file:
            for line in env_file:
                if line.startswith(f"CHANNEL_{channel_index}_ID="):
                    channel_index += 1
    except FileNotFoundError:
        print(Fore.YELLOW + ".env file not found. It will be created.")
    
    # Get channel information from user
    channel_id = input(Fore.WHITE + "Enter Channel ID (e.g., @mychannel): ")
    channel_link = input(Fore.WHITE + "Enter Channel Link (e.g., https://t.me/mychannel): ")
    
    # Append channel information to the .env file
    with open('.env', 'a') as env_file:
        env_file.write(f"CHANNEL_{channel_index}_ID={channel_id}\n")
        env_file.write(f"CHANNEL_{channel_index}_LINK={channel_link}\n")
    
    print(Fore.GREEN + f"Channel added successfully as CHANNEL_{channel_index}.")
    manage_channels()

# 1.2 Stop sending to a channel
def stop_channel():
    modify_channel_status("stop")

# 1.3 Resume sending to a channel
def resume_channel():
    modify_channel_status("resume")

# 1.4 Remove a channel
def remove_channel():
    modify_channel_status("remove")

# Modify channel status (stop, resume, or remove)
def modify_channel_status(action):
    channels = {}
    with open('.env', 'r') as env_file:
        lines = env_file.readlines()
    
    # Collect channels from the .env file
    for line in lines:
        if line.startswith("CHANNEL_") and "_ID" in line:
            key = line.split('=')[0]
            channel_id = line.split('=')[1].strip()
            channels[key] = channel_id
    
    # Display available channels
    print(Fore.GREEN + "Available Channels:")
    for idx, (key, channel_id) in enumerate(channels.items(), start=1):
        print(Fore.WHITE + f"{idx}." + Fore.GREEN + f" {channel_id}")
    
    choice = int(input(Fore.WHITE + "Select a channel by number: "))
    selected_key = list(channels.keys())[choice - 1]
    
    # Edit channels based on the selected action
    with open('.env', 'w') as env_file:
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
    interval = input(Fore.WHITE + "Enter post interval in minutes (default is 30): ") or "30"
    start_time = input(Fore.WHITE + "Enter start time (HH:mm, default is 08:00): ") or "08:00"
    end_time = input(Fore.WHITE + "Enter end time (HH:mm, default is 24:00): ") or "24:00"
    
    # Create service file
    service_content = f"""[Unit]
Description=Run Xtream UI Bot Script
After=network.target

[Service]
WorkingDirectory=/opt/xtream-ui_bot/core
ExecStart=/usr/bin/python3 massage.py
Environment="PATH=/usr/bin:/usr/local/bin"
Restart=on-failure
User=root
Group=root

[Install]
WantedBy=multi-user.target
"""
    with open("/etc/systemd/system/xtream-ui_bot.service", 'w') as service_file:
        service_file.write(service_content)
    
    # Create timer file
    timer_content = f"""[Unit]
Description=Run Xtream UI Bot Script every {interval} minutes between {start_time} and {end_time}

[Timer]
Unit=xtream-ui_bot.service
OnBootSec=5min
OnUnitActiveSec={interval}min
Persistent=true

[Install]
WantedBy=timers.target
"""
    with open("/etc/systemd/system/xtream-ui_bot.timer", 'w') as timer_file:
        timer_file.write(timer_content)
    
    # Reload and enable systemd services
    os.system("systemctl daemon-reload")
    os.system("systemctl enable xtream-ui_bot.timer")
    os.system("systemctl start xtream-ui_bot.timer")
    
    print(Fore.GREEN + "Post timing management configured successfully.")
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

# Unistall
def uninstall_bot():
    # Confirm uninstallation
    confirmation = input(Fore.RED + "Are you sure you want to uninstall xtream-ui bot? (y/n): ").strip().lower()
    if confirmation != "y":
        print(Fore.YELLOW + "Uninstallation cancelled.")
        main()
        return  # Exit the uninstall function

    try:
        print(Fore.RED + "Uninstalling xtream-ui bot...")

        # Stop and disable the systemd service if it exists
        service_name = "xtream-ui_bot.service"
        timer_name = "xtream-ui_bot.timer"

        print(Fore.YELLOW + "Stopping and disabling the bot service...")
        subprocess.run(['systemctl', 'stop', service_name], check=False)
        subprocess.run(['systemctl', 'disable', service_name], check=False)
        subprocess.run(['systemctl', 'stop', timer_name], check=False)
        subprocess.run(['systemctl', 'disable', timer_name], check=False)

        # Remove the service and timer files
        print(Fore.YELLOW + "Removing service and timer files...")
        service_file_path = f"/etc/systemd/system/{service_name}"
        timer_file_path = f"/etc/systemd/system/{timer_name}"
        if os.path.exists(service_file_path):
            os.remove(service_file_path)
        if os.path.exists(timer_file_path):
            os.remove(timer_file_path)

        # Reload systemd daemon
        subprocess.run(['systemctl', 'daemon-reload'], check=False)

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
