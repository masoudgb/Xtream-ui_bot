import requests
from io import BytesIO
import logging
import time  # Adding module for delay management

# Setting color format for logs
WHITE = "\033[97m"
LIGHT_ICE_BLUE = "\033[96m"  # Light icy blue
RESET = "\033[0m"

def send_photo_to_telegram(image_url: str, caption: str, TELEGRAM_TOKEN: str, CHANNEL_ID: str, parse_mode=None):
    """
    Sends a photo with a caption to Telegram.

    Args:
        image_url (str): The URL of the image to send.
        caption (str): The caption text.
        TELEGRAM_TOKEN (str): The Telegram bot token.
        CHANNEL_ID (str): The Telegram channel ID.
        parse_mode (str, optional): Message formatting type (Markdown or HTML).
    """
    try:
        response = requests.get(image_url)
        if response.status_code == 200:
            image_file = BytesIO(response.content)
            url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendPhoto"
            payload = {
                "chat_id": CHANNEL_ID,
                "caption": caption
            }
            if parse_mode:
                payload["parse_mode"] = parse_mode  # Setting message formatting
            files = {"photo": image_file}
            response = requests.post(url, data=payload, files=files)
            if response.status_code == 200:
                logging.info(f"{WHITE}Message sent successfully!{RESET}")
                logging.info(f"{LIGHT_ICE_BLUE}Channel ID: {CHANNEL_ID}{RESET}")
                time.sleep(3)  # Adding a 3-second delay
            else:
                logging.error(f"Failed to send message: {response.text}")
        else:
            logging.error(f"Failed to fetch image from URL: {image_url}")
    except Exception as e:
        logging.error(f"Error sending message to Telegram: {e}")
