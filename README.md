در اینجا تمام متن را با همان قالب‌بندی که درخواست کردید بازنویسی کرده‌ام:

# Xtream-UI Bot

**A bot to automatically post movie and series posters and information from Xtream-UI server to Telegram channels.**

---

## Features

- Automatically posts newly added movies and series from your Xtream-UI server.
- Highly customizable for posting intervals and Telegram channels.
- Supports multiple channels with separate configurations.

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/masoudgb/Xtream-ui_bot.git /opt/xtream-ui_bot
   cd /opt/xtream-ui_bot

2. Run the installation script:

python3 main.py




---

Running the Bot

To start the bot, execute:

python3 /opt/xtream-ui_bot/main.py


---

Configuration

Telegram Setup

Provide these details during setup:

Xtream-UI API URL: Example: http://yourserver:8080

API Username and Password

Telegram Bot Token: Get from BotFather

Channel IDs: Add public or private channels.


Default Posters

Configure fallback images for content missing custom covers.


---

Automating the Bot

Systemd Integration

The bot includes a systemd service and timer:

Service: Runs the bot.

Timer: Automates posting at intervals (default: 30 minutes).


Activated automatically during installation.


---

Updating the Bot

Run the following to update the bot:

python3 /opt/xtream-ui_bot/update.py


---

Troubleshooting

1. Incorrect Display on GitHub:

Ensure your file has the .md extension.

Open the file in GitHub to confirm proper formatting.



2. Broken Links:

Check syntax:

[Link Text](https://example.com)



3. Font Issues:

Use a Markdown-compatible editor (e.g., Typora, Obsidian, or VSCode).





---

Example Links in Markdown:

Xtream-UI GitHub

Telegram BotFather


**توضیح:** این نسخه از Markdown کاملاً بهینه‌سازی شده است تا هنگام مشاهده در GitHub یا سایر مرورگرهای Markdown سازگار، درست نمایش داده شود. اگر همچنان مشکلی دارید، لطفاً توضیح بیشتری ارائه کنید تا کمک بیشتری ارائه شود.

