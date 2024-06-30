# Roblox-notify-tracker

Roblox Status Monitor is a Python script designed to track the online status changes of specified Roblox users. It utilizes the Roblox API to fetch user presence and display names, sending desktop notifications via the `plyer` library upon status updates. Ensure secure handling of your Roblox authentication cookie.

### Roblox Status Monitor

**Overview:**
The Roblox Status Monitor is a Python script that monitors changes in the online status of selected Roblox users and sends desktop notifications when changes occur. It interacts with Roblox's API endpoints to retrieve real-time presence data and display names, and leverages the `plyer` library for notification delivery.

**Features:**

1. **User Presence Monitoring:**
   - Continuously checks the online status (presence) of specified Roblox users.
   - Uses Roblox API to fetch real-time presence information.

2. **Status Change Detection:**
   - Tracks changes in the online status (presence) of each monitored user.
   - Compares current status with previous status to detect updates.

3. **Notification System:**
   - Sends desktop notifications using `plyer` library upon detecting a status change.
   - Notifications include user's display name, new status, and time of the update.

4. **Robust Error Handling:**
   - Implements error handling for HTTP requests to manage network issues or API errors gracefully.
   - Logs errors to provide visibility into failed API requests or other issues.

5. **Customizable Configuration:**
   - Allows customization of Roblox authentication cookie (`roblox_cookie`) for secure API access.
   - Users can define the list of Roblox user IDs (`user_ids`) they want to monitor.

**Usage:**
- **Setup:** Replace the placeholder `roblox_cookie` with your Roblox authentication cookie at **line 56**. Keep the cookie secure and private.
- **Execution:** Run the script to start monitoring specified Roblox users. Configure user IDs at **line 58**.
- **Notifications:** Desktop notifications are generated upon status changes (e.g., user goes offline or changes location).

**Security Note:**
- Ensure your Roblox authentication cookie (`roblox_cookie`) remains confidential and is not shared publicly or stored insecurely.

**Compatibility:**
- Compatible with platforms supporting Python and `plyer` for notifications, including Windows, macOS, and Linux.

**Disclaimer:**
This script is for personal and educational purposes to demonstrate API interaction and notification systems. Comply with Roblox's terms of service and API usage policies when using such scripts.
