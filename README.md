# Roblox-notify-tracker
Roblox Status Monitor is a Python script tracking online status changes of specified Roblox users. It uses Roblox API to fetch user presence and display names, sending desktop notifications via plyer library upon status updates. Ensure secure use of your Roblox authentication cookie

### Roblox Status Monitor

**Overview:**
The Roblox Status Monitor is a Python script designed to monitor the online status changes of specified Roblox users and send desktop notifications when changes occur. It utilizes Roblox's API endpoints to fetch user presence data and user display names, and uses the `plyer` library for notifications.

**Features:**

1. **User Presence Monitoring:**
   - The program continuously checks the presence status (online location) of selected Roblox users.
   - It queries the Roblox API to retrieve real-time data about user presence.

2. **Status Change Detection:**
   - Tracks changes in the online location (presence status) of each monitored user.
   - Compares the current status with the last known status to detect updates.

3. **Notification System:**
   - Generates desktop notifications using `plyer` to inform the user when a monitored user's status changes.
   - Each notification includes the user's display name, the new status, and the time of the update.

4. **Robust Error Handling:**
   - Implements error handling for HTTP requests to manage potential network issues or API errors gracefully.
   - Logs errors to provide visibility into failed API requests or other issues.

5. **Customizable Configuration:**
   - Allows users to specify their own Roblox authentication cookie (`roblox_cookie`) to access the necessary API endpoints securely.
   - Users can define the list of Roblox user IDs (`user_ids`) they wish to monitor.

**Usage:**
- **Setup:** Replace the placeholder `roblox_cookie` with your own Roblox authentication cookie. Ensure the cookie is kept secure and not shared publicly.
- **Execution:** Run the script, and it will start monitoring the specified Roblox users.
- **Notifications:** Whenever a change in status is detected (e.g., user goes offline or changes location), a desktop notification will be displayed.

**Security Note:**
- It's crucial to keep your Roblox authentication cookie (`roblox_cookie`) confidential and not share it publicly or in unsecured environments.

**Compatibility:**
- The program is designed to work on various platforms that support Python and `plyer` for notifications, including Windows, macOS, and Linux.

**Disclaimer:**
This script is intended for personal use and educational purposes to demonstrate API interaction and notification systems. Ensure compliance with Roblox's terms of service and API usage policies when using such scripts.
