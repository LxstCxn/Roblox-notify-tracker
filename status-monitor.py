from plyer import notification
from datetime import datetime
import requests
import logging
import json
import time

config = json.load(open("config.json", 'r'))
keys = list(config.keys())

# Verify config
if "RBX_COOKIE" not in keys: exit("RBX_COOKIE is not in config file")
if config["RBX_COOKIE"] == "": exit("You must set a RBX_COOKIE")

if "UIDs" not in keys: exit("UIDs is not in config file")
if config["UIDs"] == []: exit("You add at least one ID to UIDs")

if "UPDATE_RATE" not in keys: exit("UPDATE_RATE is not in config file")
if not config["UPDATE_RATE"].isnumeric(): exit("UPDATE_RATE is not a numeric")

logging.basicConfig(level=logging.INFO)  # Logging configuration

# Function to fetch user presences
def get_user_presences(user_ids):
    url = "https://presence.roblox.com/v1/presence/users"
    headers = {
        "Content-Type": "application/json",
        "Cookie": config["RBX_COOKIE"]
    }
    data = {"userIds": user_ids}

    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()
        return response.json()["userPresences"]
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to fetch user presences: {e}")
        return None

# Function to fetch user display name
def get_user_display_name(user_id):
    url = f"https://users.roblox.com/v1/users/{user_id}"
    headers = {"Cookie": config["RBX_COOKIE"]}

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
    last_known_statuses = {user_id: None for user_id in config["UIDs"]}

    while True:
        user_presences = get_user_presences(config["UIDs"])

        if user_presences:
            for presence in user_presences:
                user_id = presence["userId"]
                last_location = presence["lastLocation"]

                if last_known_statuses[user_id] != last_location:
                    last_known_statuses[user_id] = last_location
                    display_name = get_user_display_name(user_id)

                    if display_name:
                        send_notification(display_name, last_location)

        time.sleep(config["UPDATE_RATE"])