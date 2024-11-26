import time
import json
import os
import logging
from core.api_client import get_vod_data, get_vod_info, get_vod_categories
from core.telegram import send_photo_to_telegram
from config.config import DEFAULT_VOD_COVER_URL  # Importing default cover for VOD
from config.config import CHANNELS  # Importing channels from config

# Path to the JSON file for storing sent movie IDs
MOVIES_FILE = "/opt/xtream-ui_bot/core/movies.json"

# Temporary set to store sent movie IDs
temp_sent_movie_ids = set()

# Load sent movie IDs from the JSON file
def load_sent_movie_ids():
    if os.path.exists(MOVIES_FILE):
        with open(MOVIES_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    return []  # If file does not exist, return an empty list

# Save sent movie IDs to the JSON file
def save_sent_movie_ids(ids):
    with open(MOVIES_FILE, "w", encoding="utf-8") as file:
        json.dump(ids, file, ensure_ascii=False, indent=4)

# Retrieve the name of the movie category
def get_vod_category_name(category_id, categories):
    for category in categories:
        if category.get("category_id") == category_id:
            return category.get("category_name", "Unknown")
    return "Unknown"

# Send notification to Telegram with retry mechanism
def send_to_telegram_with_retry(image_url, caption, TELEGRAM_TOKEN, CHANNEL_ID, retries=3):
    for attempt in range(1, retries + 1):
        try:
            send_photo_to_telegram(image_url, caption, TELEGRAM_TOKEN, CHANNEL_ID, parse_mode="HTML")
            return True  # Successfully sent
        except Exception as e:
            logging.error(f"Failed to send to Telegram (Attempt {attempt}/{retries}): {e}")
            time.sleep(5)  # Pause between retries
    return False  # Failed after all retries

# Notify about a new VOD
def notify_for_vod(vod_id, vod_name, vod_info, vod_cover, category_id, categories, TELEGRAM_TOKEN, CHANNEL_ID, CHANNEL_LINK):
    global temp_sent_movie_ids  # Use the temporary set

    # Category information
    category = get_vod_category_name(category_id, categories)

    # Movie information
    vod_duration = vod_info.get("info", {}).get("duration", "N/A")
    vod_director = vod_info.get("info", {}).get("director", "Unknown")
    vod_rating = vod_info.get("info", {}).get("rating", "N/A")
    vod_country = vod_info.get("info", {}).get("country", "Unknown")
    vod_plot = vod_info.get("info", {}).get("plot", "No plot available.")

    # Notification caption
    caption = (
        f"🎥 <b>New Movie Added: {vod_name}!</b>\n\n"
        f"🎬 Category: <b>{category}</b>\n\n"
        f"🌍 Country: <b>{vod_country}</b>\n"
        f"🎭 Director: <b>{vod_director}</b>\n"
        f"⏳ Duration: {vod_duration}\n"
        f"⭐ Rating: {vod_rating}\n\n"
        f"📝 Plot:\n{vod_plot}\n\n"
        f"🔗 Channel Link: <a href='{CHANNEL_LINK}'>Here</a>"
    )

    vod_image = vod_cover if vod_cover else DEFAULT_VOD_COVER_URL

    # Send to Telegram
    return send_to_telegram_with_retry(vod_image, caption, TELEGRAM_TOKEN, CHANNEL_ID)

# Check and notify about new VODs
def check_and_notify_new_vod(API_URL, USERNAME, PASSWORD, TELEGRAM_TOKEN, CHANNELS):
    global temp_sent_movie_ids

    # Check if it's the first run
    is_first_run = not os.path.exists(MOVIES_FILE)

    # Load previously sent movie IDs
    sent_movie_ids = set(load_sent_movie_ids())  # This will load an empty list if file doesn't exist

    # Fetch categories
    categories = get_vod_categories(API_URL, USERNAME, PASSWORD)
    if not categories:
        logging.error("No categories data received.")
        return

    # Fetch VOD data
    vod_data = get_vod_data(API_URL, USERNAME, PASSWORD)
    if vod_data:
        if is_first_run:
            # On the first run, save all VOD IDs directly
            first_run_ids = {vod.get("stream_id") for vod in vod_data if vod.get("stream_id") is not None}
            save_sent_movie_ids(list(first_run_ids))  # Save all IDs immediately
            logging.info("First run: Saved all VOD IDs.")
        else:
            for vod in vod_data:
                vod_id = vod.get("stream_id")
                if vod_id is None or vod_id in sent_movie_ids:
                    continue  # Skip already sent or invalid IDs

                # Movie details
                vod_name = vod.get("name", "Unknown Movie")
                vod_cover = vod.get("stream_icon", None)
                category_id = vod.get("category_id", 0)
                vod_info = get_vod_info(API_URL, USERNAME, PASSWORD, vod_id)

                if vod_info:
                    # Flag to track successful notifications
                    successfully_sent = True

                    # Send movie notification to all channels
                    for channel in CHANNELS:
                        success = notify_for_vod(vod_id, vod_name, vod_info, vod_cover, category_id, categories, TELEGRAM_TOKEN, channel['id'], channel['link'])
                        if not success:
                            successfully_sent = False  # If one fails, mark as failed

                    # If successfully sent to all channels, add to sent_movie_ids
                    if successfully_sent:
                        temp_sent_movie_ids.add(vod_id)

            # Save the updated list of sent IDs after notifying all channels
            sent_movie_ids.update(temp_sent_movie_ids)
            save_sent_movie_ids(list(sent_movie_ids))  # Save updated list
            temp_sent_movie_ids.clear()  # Clear the temporary set
