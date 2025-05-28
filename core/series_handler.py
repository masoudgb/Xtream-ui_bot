import time
import json
import os
import logging
from core.api_client import get_series_data, get_series_info, get_categories
from core.telegram import send_photo_to_telegram
from config.config import DEFAULT_SERIES_COVER_URL  # Importing default cover from config.py

# Path to the JSON file for storing sent series information
SERIES_FILE = "/opt/xtream-ui_bot/core/series.json"

# Load sent series information from the JSON file
def load_sent_series():
    if os.path.exists(SERIES_FILE):
        with open(SERIES_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    return {}

# Save sent series information to the JSON file
def save_sent_series(sent_series):
    with open(SERIES_FILE, "w", encoding="utf-8") as file:
        json.dump(sent_series, file, ensure_ascii=False, indent=4)

# Send to Telegram with retry mechanism
def send_to_telegram_with_retry(image_url, caption, TELEGRAM_TOKEN, CHANNEL_ID, retries=3):
    for attempt in range(1, retries + 1):
        try:
            send_photo_to_telegram(image_url, caption, TELEGRAM_TOKEN, CHANNEL_ID, parse_mode="HTML")
            return True  # Sent successfully
        except Exception as e:
            logging.error(f"Error sending to Telegram (attempt {attempt}/{retries}): {e}")
            time.sleep(5)  # Pause between attempts
    return False  # Failed after all retries

# Compare episodes and send notifications
def compare_and_notify(series_id, series_name, new_episodes, old_episodes, series_cover, category_name, TELEGRAM_TOKEN, CHANNELS, sent_series):
    is_new = False
    series_updates = {}  # Store updates for saving after sending

    if not isinstance(new_episodes, dict):
        logging.error(f"Invalid format for new episodes of series {series_id}. Expected dict, got {type(new_episodes)}.")
        return is_new

    for season_num, episodes in new_episodes.items():
        if not isinstance(episodes, list):
            logging.error(f"Invalid format for episodes of season {season_num}. Expected list, got {type(episodes)}.")
            continue

        old_season_episodes = old_episodes.get(str(season_num), [])
        new_episode_nums = [ep.get("episode_num") for ep in episodes if ep.get("episode_num") not in old_season_episodes]

        if not new_episode_nums:
            continue  # No new episodes

        # Prepare caption information
        season_is_new = str(season_num) not in old_episodes
        episode_count = len(new_episode_nums)

        if season_is_new:
            episode_info = f"Season {season_num} with {episode_count} episode{'s' if episode_count > 1 else ''}"
        elif episode_count == 1:
            episode = next(ep for ep in episodes if ep.get("episode_num") == new_episode_nums[0])
            episode_title = episode.get("title", "No Title")
            episode_info = f"Episode {new_episode_nums[0]} of Season {season_num} ({episode_title})"
        else:
            episode_info = f"Episodes {min(new_episode_nums)} to {max(new_episode_nums)} of Season {season_num}"

        for channel in CHANNELS:
            channel_link = channel.get("link", "#")
            rtl_character = "\u200F"

            # Notification caption
            caption = (
                rtl_character +
                f"🎬 <b>Update for {series_name}!</b>\n\n"
                f"📌 {episode_info} added!\n\n"
                f"🎭 Category: <b>{category_name}</b>\n\n"
                f"🔗 Channel Link: <a href='{channel_link}'>Here</a>"
            )

            # Use series cover or default cover
            series_image = series_cover if series_cover else DEFAULT_SERIES_COVER_URL

            # Send to Telegram
            if not send_to_telegram_with_retry(series_image, caption, TELEGRAM_TOKEN, channel["id"]):
                logging.error(f"Failed to send update for season {season_num} of series {series_id} to channel {channel['id']}.")
                break
        else:
            is_new = True
            if str(season_num) not in series_updates:
                series_updates[str(season_num)] = []
            series_updates[str(season_num)].extend(new_episode_nums)

    # Add updates to sent_series after sending to all channels
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

    # Load sent series information
    sent_series = load_sent_series()

    # Fetch categories
    categories = get_categories(API_URL, USERNAME, PASSWORD)
    if not categories:
        logging.error("No category data received.")
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
                    # On first run, only store data
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
                logging.warning(f"No episodes found for series {series_id}.")
    else:
        logging.error("No data received from API.")

    # Save updated state
    save_sent_series(sent_series)
