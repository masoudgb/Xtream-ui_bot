
---

Xtream-UI Bot

A powerful bot using the Xtream-UI API to automatically post movie and series posters along with information from your Xtream-UI server directly to Telegram channels.

Features

Posts movies and series added to your Xtream-UI server automatically.

Fully customizable settings, including Telegram channels and posting intervals.

Supports multiple channels with unique configurations.

Share your content with rich visual details effortlessly.


Requirements

Root Access: Required for installing and configuring the bot.

Operating System: Ubuntu 20.04 or newer recommended.

Python: Python 3.x with pip installed.



---

Installation

Follow the steps below to install the bot:

1. Clone the repository:

git clone https://github.com/masoudgb/Xtream-ui_bot.git /opt/xtream-ui_bot
cd /opt/xtream-ui_bot


2. Run the bot setup:

python3 main.py




---

Running the Bot

After installation, start the bot using:

python3 /opt/xtream-ui_bot/main.py

You can manage the bot and its settings through the interactive menu.


---

Menu Options

The bot includes the following options:

1. Install Xtream-UI Bot: For new installations.


2. Manage Xtream-UI Bot: Edit channels, post intervals, and more.


3. Update Xtream-UI Bot: Update the bot to the latest version.


4. Uninstall Xtream-UI Bot: Completely remove the bot and all configurations.


5. Exit: Exit the script.




---

Configuration Details

Telegram Settings

During installation, the bot will ask for:

Xtream-UI API URL (e.g., http://yourserver:8080)

API Username and Password

Telegram Bot Token (create your bot using BotFather)

Channel IDs: Include both private/public channels.


Post Timing

Control posting schedules using the Manage Post Timing option. You can set specific intervals or times for content sharing.

Default Cover Images

The bot supports setting default covers for movies and series that do not include custom posters.


---

Updating the Bot

To update the bot, select the Update Xtream-UI Bot option in the menu. This will pull the latest code while preserving your settings.


---

Uninstallation

To completely remove the bot:

Select the Uninstall Xtream-UI Bot option from the menu.

It will clean up all services and files.



---

System Requirements

The bot automatically installs required Python libraries, including:

python-telegram-bot

termcolor

python-dotenv

requests



---

Automation (Systemd Service)

The bot uses a systemd service and timer for automatic execution:

Service: Runs the bot.

Timer: Defines posting intervals (default: 30 minutes).


These are configured and activated during installation.


---

Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.


---

License

This project is licensed under the MIT License. For details, see the LICENSE file.


---

Contact

For questions or support, you can reach out via:

GitHub: MasoudGB

Telegram: [Your Telegram Handle]



---

Copy and paste this markdown into your GitHub repository’s README.md file. Let me know if you need further assistance!

