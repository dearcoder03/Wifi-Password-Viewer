# only list of old wifi abd password

import subprocess

def get_wifi_passwords():
    # Get the list of all WiFi profiles
    profiles_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors='ignore').split('\n')
    profiles = [line.split(":")[1][1:-1] for line in profiles_data if "All User Profile" in line]

    wifi_passwords = []

    for profile in profiles:
        # Get the WiFi password for each profile
        profile_info = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', profile, 'key=clear']).decode('utf-8', errors='ignore').split('\n')
        password = None
        for line in profile_info:
            if "Key Content" in line:
                password = line.split(":")[1][1:-1]
                break
        wifi_passwords.append({'SSID': profile, 'Password': password})

    return wifi_passwords

# Get WiFi passwords and print them
passwords = get_wifi_passwords()
for wifi in passwords:
    print(f"SSID: {wifi['SSID']}, Password: {wifi['Password']}")
