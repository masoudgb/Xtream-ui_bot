مشکلی که در مورد عدم نمایش صحیح فرمت Markdown در GitHub یا هنگام کپی و پیست کردن رخ می‌دهد، معمولاً ناشی از تنظیمات مرورگر یا برنامه‌ای است که برای مشاهده محتوا استفاده می‌کنید. با این حال، برای اطمینان از نمایش صحیح، چند نکته و نسخه بهینه شده Markdown ارائه می‌شود.


---

رفع مشکلات Markdown:

1. استفاده از GitHub به‌عنوان رندر نهایی:
Markdown به‌صورت استاندارد در GitHub بهترین نمایش را دارد. اگر لینک‌ها یا استایل درست نمایش داده نمی‌شوند:

حتماً فایل خود را با پسوند .md ذخیره کنید.

آن را در GitHub آپلود کنید و از همانجا مشاهده کنید.



2. تنظیمات فونت در GitHub یا ویرایشگرها:
اگر هنگام کپی و پیست متن به مرورگر یا یک ویرایشگر، قالب به هم می‌ریزد:

اطمینان حاصل کنید که فرمت Markdown توسط ویرایشگر پشتیبانی می‌شود.

از ویرایشگرهای Markdown مثل VSCode یا Typora برای بررسی استفاده کنید.





---

نسخه نهایی Markdown:

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



---

نکته: اگر پس از این، مشکل همچنان پابرجا بود، لطفاً نوع مرورگر یا ویرایشگری که استفاده می‌کنید را بفرمایید تا بررسی دقیق‌تر انجام شود.

