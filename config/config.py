import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# API information (loaded from environment variables)
API_URL = os.getenv("API_URL")
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

# Telegram bot information (loaded from environment variables)
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

# Default cover image URLs (loaded from environment variables)
DEFAULT_VOD_COVER_URL = os.getenv("DEFAULT_VOD_COVER_URL")  # First load VOD cover
DEFAULT_SERIES_COVER_URL = os.getenv("DEFAULT_SERIES_COVER_URL")  # Then load Series cover

# Channel information (loaded from environment variables)
CHANNELS = []

# Function to load channels from environment variables
def load_channels():
    channel_index = 1
    while True:
        # Fetching channel data from environment variables as CHANNEL_X_ID and CHANNEL_X_LINK
        channel_id = os.getenv(f"CHANNEL_{channel_index}_ID")
        channel_link = os.getenv(f"CHANNEL_{channel_index}_LINK")
        
        # If the channel does not exist, break the loop
        if not channel_id or not channel_link:
            break
        
        # Add channel to the list
        CHANNELS.append({"id": channel_id, "link": channel_link})
        channel_index += 1

# Load channels from environment variables
load_channels()
