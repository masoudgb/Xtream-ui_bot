Here is a detailed and complete README.md for your GitHub project:

# Xtream-UI Bot

A powerful bot leveraging the original **Xtream-UI API** to post movie and series posters along with relevant information from your Xtream-UI server directly to your Telegram channels.

## Features

- Automatically posts movies and series added to your Xtream-UI server.
- Highly customizable settings, including channel management and post intervals.
- Supports multiple Telegram channels.
- Simplifies the sharing of your server's content with rich visual and textual data.

## Requirements

- **Root Access**: Required for installation and service setup.
- **Operating System**: Recommended: Ubuntu 20.04 or higher.
- **Python**: Python 3.x with pip installed.

## Installation

To install and set up the bot, run the following commands in your terminal:

```bash
git clone https://github.com/masoudgb/Xtream-ui_bot.git /opt/xtream-ui_bot && cd /opt/xtream-ui_bot && python3 main.py

Running the Bot

After installation, you can start the bot by executing:

python3 /opt/xtream-ui_bot/main.py

Post Configuration

Once installed, configure the post timing and channels using the menu provided within the script to start posting.

Installation Steps in Detail

1. Download the repository:

Clone the project into the /opt directory and navigate to it:

git clone https://github.com/masoudgb/Xtream-ui_bot.git /opt/xtream-ui_bot
cd /opt/xtream-ui_bot


2. Run the installer:

Start the script to install dependencies and configure the bot:

python3 main.py


3. Provide necessary details:

During installation, you’ll be prompted to enter:

API URL (e.g., http://yourserver.com:8080)

Username and Password for Xtream-UI

Telegram Bot Token

Default cover URLs for VOD and Series

Telegram Channel IDs and links



4. Manage Channels and Timing:

Use the Manage Post Timing option to set the schedule for posting content.



Menu Options

The bot provides the following options in its main menu:

1. Install Xtream-UI Bot: For a fresh installation.


2. Manage Xtream-UI Bot: To manage channels, post timings, and bot behavior.


3. Update Xtream-UI Bot: Pull the latest updates from the repository.


4. Uninstall: Completely remove the bot and its configurations.


5. Exit: Exit the script.



Customization Options

Managing Channels

You can add, remove, or pause/resume sending to Telegram channels via the Manage Channels menu.

Configuring Post Timing

Set custom intervals and active hours for content posting to better align with your audience.

Updating the Bot

Update the bot effortlessly by selecting Update Xtream-UI Bot in the menu. This pulls the latest changes from the GitHub repository while preserving your settings.

Uninstallation

To uninstall the bot completely:

Select the Uninstall option from the menu.

It will stop the service, delete the files, and clean up the environment.


System Requirements

Python Libraries:

python-telegram-bot

termcolor

python-dotenv

requests



The script automatically installs these libraries during the setup.

Service and Timer Configuration

To automate the bot, the script creates a systemd service and timer:

Service: Handles the bot execution.

Timer: Defines the interval for posting (default: every 30 minutes).


These are automatically enabled and started during setup.

Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve the project.

License

This project is licensed under the MIT License. See the LICENSE file for more details.

Contact

For further assistance or inquiries, contact the author at:

GitHub: MasoudGB

Telegram: [Your Telegram Handle]



---

Enjoy managing your Xtream-UI content effortlessly with Xtream-UI Bot!

This `README.md` is structured, detailed, and user-friendly for your GitHub repository. Let me know if you'd like further adjustments!

