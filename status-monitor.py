import requests
import time
from datetime import datetime
from plyer import notification
import logging
import json

logging.basicConfig(level=logging.INFO)  # Logging configuration

def config():
    with open("config.json", "r") as file:
        return json.load(file)
    
def check_config():
    required_keys = ["roblox_cookie", "user_ids", "interval"]
    config_keys = config().keys()

    for key in required_keys:
        if key not in config_keys:
            logging.error(f"Missing required key in config: {key}")
            return False
        
        if not config()[key]:
            logging.error(f"Value for key {key} is empty")
            return False
    
    if not config()["interval"] >= 1:
        logging.error("Interval value must be greater than 1")
        return False
    
    return True


# Function to fetch user presences
def get_user_presences(user_ids, roblox_cookie):
    url = "https://presence.roblox.com/v1/presence/users"
    headers = {
        "Content-Type": "application/json",
        "Cookie": f".ROBLOSECURITY={roblox_cookie}"
    }
    data = {
        "userIds": user_ids
    }

    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()
        return response.json()["userPresences"]
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to fetch user presences: {e}")
        return None

# Function to fetch user display name
def get_user_display_name(user_id, roblox_cookie):
    url = f"https://users.roblox.com/v1/users/{user_id}"
    headers = {
        "Cookie": f".ROBLOSECURITY={roblox_cookie}"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()["displayName"]
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to fetch user data: {e}")
        return None

# Function to send notification with display name and time
def send_notification(display_name, new_status):
    title = f"Status change detected for {display_name}"
    current_time = datetime.now().strftime('%H:%M')
    message = f"New status: {new_status}\nTime: {current_time}"
    notification.notify(
        title=title,
        message=message,
        app_name="Roblox Status Monitor"
    )

# Example usage with status change detection
if __name__ == "__main__":
    if not check_config():
        logging.error("Config check failed. Please check the config file and try again.")
        exit()

    roblox_cookie = config()["roblox_cookie"]
    user_ids = config()["user_ids"]
    interval = config()["interval"]

    last_known_statuses = {user_id: None for user_id in user_ids}

    while True:
        user_presences = get_user_presences(user_ids, roblox_cookie)

        if user_presences:
            for presence in user_presences:
                user_id = presence["userId"]
                last_location = presence["lastLocation"]

                if last_known_statuses[user_id] != last_location:
                    last_known_statuses[user_id] = last_location
                    display_name = get_user_display_name(user_id, roblox_cookie)

                    if display_name:
                        send_notification(display_name, last_location)

        time.sleep(interval*60)
