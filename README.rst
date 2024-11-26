Xtream-UI Bot
===============
A bot to automatically post movie and series posters and information from Xtream-UI server to Telegram channels.

Features
---------
- Automatically posts newly added movies and series from your Xtream-UI server.
- Highly customizable for posting intervals and Telegram channels.
- Supports multiple channels with separate configurations.

Installation
--------------

1. Clone the repository::

    git clone https://github.com/masoudgb/Xtream-ui_bot.git /opt/xtream-ui_bot
    cd /opt/xtream-ui_bot

2. Run the installation script::

    python3 main.py

Running the Bot
----------------
To start the bot, execute::

    python3 /opt/xtream-ui_bot/main.py

Configuration
--------------

Telegram Setup
~~~~~~~~~~~~~~~
Provide these details during setup:
- **Xtream-UI API URL**: Example: ``http://yourserver:8080``
- **API Username and Password**
- **Telegram Bot Token**: Get from `BotFather <https://core.telegram.org/bots#botfather>`_
- **Channel IDs**: Add public or private channels.

Default Posters
~~~~~~~~~~~~~~~
Configure fallback images for content missing custom covers.

Automating the Bot
-------------------

Systemd Integration
~~~~~~~~~~~~~~~~~~~~
The bot includes a *systemd* service and timer:
- **Service**: Runs the bot.
- **Timer**: Automates posting at intervals (default: 30 minutes).

Activated automatically during installation.

Updating the Bot
-----------------
Run the following to update the bot::

    python3 /opt/xtream-ui_bot/update.py

Troubleshooting
----------------

1. **Incorrect Display on GitHub:**
   Ensure your file has the ``.rst`` extension and is uploaded correctly.

2. **Broken Links:**
   Check syntax like this::
   
      `Link Text <https://example.com>`_

3. **Font Issues:**
   Use a Markdown-compatible editor (e.g., *Typora*, *Obsidian*, or *VSCode*).

Example Links
--------------
- `Xtream-UI GitHub <https://github.com/masoudgb>`_
- `Telegram BotFather <https://core.telegram.org/bots#botfather>`_
