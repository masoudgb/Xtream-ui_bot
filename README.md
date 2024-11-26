---

Xtream-UI Bot

A powerful bot using the Xtream-UI API to automatically post movie and series posters along with information from your Xtream-UI server directly to Telegram channels.


---

Features

Automatically posts movies and series added to your Xtream-UI server.

Fully customizable, including Telegram channels and posting intervals.

Supports multiple channels with unique configurations.

Effortlessly share your content with rich visual details.



---

Requirements

Root Access: Required for installing and configuring the bot.

Operating System: Ubuntu 20.04 or newer is recommended.

Python: Python 3.x with pip installed.



---

Installation

1. Clone the repository:

git clone https://github.com/masoudgb/Xtream-ui_bot.git /opt/xtream-ui_bot
cd /opt/xtream-ui_bot


2. Run the bot setup:

python3 main.py




---

Running the Bot

To start the bot:

python3 /opt/xtream-ui_bot/main.py

Manage the bot through its interactive menu.


---

Menu Options

1. Install Xtream-UI Bot: Set up the bot for the first time.


2. Manage Xtream-UI Bot: Edit settings, channels, and post intervals.


3. Update Xtream-UI Bot: Update to the latest version.


4. Uninstall Xtream-UI Bot: Completely remove the bot.


5. Exit: Exit the menu.




---

Configuration Details

Telegram Settings

During installation, provide:

Xtream-UI API URL: e.g., http://yourserver:8080

API Username and Password

Telegram Bot Token: Create your bot via BotFather

Channel IDs: Add private or public channels.


Post Timing

Set specific intervals or times for posting content via the Manage Post Timing option.

Default Cover Images

Configure default covers for movies and series missing custom posters.


---

Updating the Bot

To update, choose the Update Xtream-UI Bot option in the menu. This pulls the latest code while keeping your settings intact.


---

Uninstallation

To remove the bot:

1. Select the Uninstall Xtream-UI Bot option.


2. All services and files will be deleted.




---

System Requirements

Required Python libraries are installed automatically, including:

python-telegram-bot

termcolor

python-dotenv

requests



---

Automation (Systemd Service)

The bot uses a systemd service and timer for automation:

Service: Runs the bot.

Timer: Configures posting intervals (default: 30 minutes).


These are activated during installation.


---

Contributing

Contributions are welcome! Open an issue or submit a pull request.


---

License

This project is licensed under the MIT License. See the LICENSE file for details.


---

Contact

GitHub: MasoudGB

Telegram: [Your Telegram Handle]



---
