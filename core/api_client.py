import requests
import logging

# Fetch series data
def get_series_data(API_URL, USERNAME, PASSWORD):
    try:
        params = {
            "username": USERNAME,
            "password": PASSWORD,
            "action": "get_series"
        }
        response = requests.get(API_URL, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            logging.error(f"Failed to fetch series data: {response.text}")
            return None
    except Exception as e:
        logging.error(f"Error fetching data from API: {e}")
        return None

# Fetch series information
def get_series_info(API_URL, USERNAME, PASSWORD, series_id):
    try:
        params = {
            "username": USERNAME,
            "password": PASSWORD,
            "action": "get_series_info",
            "series_id": series_id
        }
        response = requests.get(API_URL, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            logging.error(f"Failed to fetch series info: {response.text}")
            return None
    except Exception as e:
        logging.error(f"Error fetching series info from API: {e}")
        return None

# Fetch series categories
def get_categories(API_URL, USERNAME, PASSWORD):
    try:
        params = {
            "username": USERNAME,
            "password": PASSWORD,
            "action": "get_series_categories"
        }
        response = requests.get(API_URL, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            logging.error(f"Failed to fetch categories data: {response.text}")
            return None
    except Exception as e:
        logging.error(f"Error fetching categories data from API: {e}")
        return None

# Fetch VOD data
def get_vod_data(API_URL, USERNAME, PASSWORD):
    try:
        params = {
            "username": USERNAME,
            "password": PASSWORD,
            "action": "get_vod_streams"
        }
        response = requests.get(API_URL, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            logging.error(f"Failed to fetch VOD data: {response.text}")
            return None
    except Exception as e:
        logging.error(f"Error fetching VOD data: {e}")
        return None

# Fetch specific VOD information
def get_vod_info(API_URL, USERNAME, PASSWORD, vod_id):
    try:
        params = {
            "username": USERNAME,
            "password": PASSWORD,
            "action": "get_vod_info",
            "vod_id": vod_id
        }
        response = requests.get(API_URL, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            logging.error(f"Failed to fetch VOD info: {response.text}")
            return None
    except Exception as e:
        logging.error(f"Error fetching VOD info: {e}")
        return None

# Fetch VOD categories
def get_vod_categories(API_URL, USERNAME, PASSWORD):
    try:
        params = {
            "username": USERNAME,
            "password": PASSWORD,
            "action": "get_vod_categories"
        }
        response = requests.get(API_URL, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            logging.error(f"Failed to fetch VOD categories data: {response.text}")
            return None
    except Exception as e:
        logging.error(f"Error fetching VOD categories data: {e}")
        return None
