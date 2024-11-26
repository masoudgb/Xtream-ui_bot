import time
import json
import os
import logging
from core.api_client import get_series_data, get_series_info, get_categories
from core.telegram import send_photo_to_telegram
from config.config import DEFAULT_SERIES_COVER_URL  # Importing default cover from config.py

# Path to the JSON file for storing sent series data
SERIES_FILE = "/opt/xtream-ui_bot/core/series.json"

# Load sent series data from the JSON file
def load_sent_series():
    if os.path.exists(SERIES_FILE):
        with open(SERIES_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    return {}

# Save sent series data to the JSON file
def save_sent_series(sent_series):
    with open(SERIES_FILE, "w", encoding="utf-8") as file:
        json.dump(sent_series, file, ensure_ascii=False, indent=4)

# Send to Telegram with retry mechanism
def send_to_telegram_with_retry(image_url, caption, TELEGRAM_TOKEN, CHANNEL_ID, retries=3):
    for attempt in range(1, retries + 1):
        try:
            send_photo_to_telegram(image_url, caption, TELEGRAM_TOKEN, CHANNEL_ID, parse_mode="HTML")
            return True  # Successfully sent
        except Exception as e:
            logging.error(f"Failed to send to Telegram (Attempt {attempt}/{retries}): {e}")
            time.sleep(5)  # Pause between retries
    return False  # Failed after all retries

# Compare new episodes and notify
def compare_and_notify(series_id, series_name, new_episodes, old_episodes, series_cover, category_name, TELEGRAM_TOKEN, CHANNELS, sent_series):
    is_new = False
    series_updates = {}  # Store updates for later saving after notifying all channels

    if not isinstance(new_episodes, dict):
        logging.error(f"Invalid new_episodes format for series ID {series_id}. Expected dict, got {type(new_episodes)}.")
        return is_new

    for season_num, episodes in new_episodes.items():
        if not isinstance(episodes, list):
            logging.error(f"Invalid episodes format for season {season_num}. Expected list, got {type(episodes)}.")
            continue

        old_season_episodes = old_episodes.get(str(season_num), [])

        for episode in episodes:
            episode_num = episode.get("episode_num")
            if episode_num in old_season_episodes:
                continue  # Already sent

            # Episode details
            episode_title = episode.get("title", "Untitled")
            episode_duration = episode.get("info", {}).get("duration", "N/A")
            episode_rating = episode.get("info", {}).get("rating", "n/a")
            episode_rating = f"{episode_rating}/10" if episode_rating and episode_rating != "n/a" else "n/a"

            for channel in CHANNELS:
                channel_link = channel.get("link", "#")
                caption = (
                    f"🎬 <b>Episode {episode_num} of Season {season_num} from the series {series_name} is now available!</b>\n\n"
                    f"📌 Title: <b>{episode_title}</b>\n\n"
                    f"🎭 Category: <b>{category_name}</b>\n\n"
                    f"⏳ Duration: {episode_duration}\n\n"
                    f"⭐ Rating: {episode_rating}\n\n\n"
                    f"🔗 Channel Link: <a href='{channel_link}'>Here</a>"
                )

                # Use the series cover or default cover if none is available
                series_image = series_cover if series_cover else DEFAULT_SERIES_COVER

                # Send to Telegram
                if not send_to_telegram_with_retry(series_image, caption, TELEGRAM_TOKEN, channel["id"]):
                    logging.error(f"Failed to send episode {episode_num} of season {season_num} for series ID {series_id} to channel {channel['id']}.")
                    break
            else:
                is_new = True
                if str(season_num) not in series_updates:
                    series_updates[str(season_num)] = []
                series_updates[str(season_num)].append(episode_num)

    # Add updates to sent_series after notifying all channels
    for season_num, episodes in series_updates.items():
        if str(series_id) not in sent_series:
            sent_series[str(series_id)] = {"seasons": {}}
        if season_num not in sent_series[str(series_id)]["seasons"]:
            sent_series[str(series_id)]["seasons"][season_num] = []
        sent_series[str(series_id)]["seasons"][season_num].extend(episodes)

    return is_new

# Check and notify about new series
def check_and_notify_new_series(API_URL, USERNAME, PASSWORD, TELEGRAM_TOKEN, CHANNELS):
    is_first_run = not os.path.exists(SERIES_FILE)

    # Load previously sent series data
    sent_series = load_sent_series()

    # Fetch categories
    categories = get_categories(API_URL, USERNAME, PASSWORD)
    if not categories:
        logging.error("No categories data received.")
        return

    # Fetch series data
    series_data = get_series_data(API_URL, USERNAME, PASSWORD)
    if series_data:
        for series in series_data:
            series_id = series.get("series_id")
            series_name = series.get("name", "Unknown Series")
            series_cover = series.get("cover", None)
            category_id = series.get("category_id", 0)

            # Get category name
            category_name = next(
                (cat.get("category_name", "Unknown") for cat in categories if cat.get("category_id") == category_id),
                "Unknown",
            )

            # Fetch new episodes
            series_info = get_series_info(API_URL, USERNAME, PASSWORD, series_id)
            if series_info and "episodes" in series_info:
                new_episodes = series_info["episodes"]

                # Previously sent episodes
                old_episodes = sent_series.get(str(series_id), {}).get("seasons", {})

                if is_first_run:
                    # If it's the first run, just save the data
                    if str(series_id) not in sent_series:
                        sent_series[str(series_id)] = {"seasons": {}}
                    sent_series[str(series_id)]["seasons"] = {
                        str(season_num): [ep.get("episode_num") for ep in episodes]
                        for season_num, episodes in new_episodes.items()
                    }
                else:
                    # Compare and send notifications
                    compare_and_notify(series_id, series_name, new_episodes, old_episodes, series_cover, category_name, TELEGRAM_TOKEN, CHANNELS, sent_series)
            else:
                logging.warning(f"No episodes found for series ID {series_id}.")
    else:
        logging.error("No data received from API.")

    # Save updated state
    save_sent_series(sent_series)
