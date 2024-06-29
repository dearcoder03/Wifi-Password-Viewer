import subprocess
import streamlit as st

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

# Streamlit app
st.title("WiFi Password Viewer")

st.write("This application will show you the SSID and passwords of all saved WiFi profiles on your device.")

passwords = get_wifi_passwords()

if passwords:
    for wifi in passwords:
        st.write(f"**SSID:** {wifi['SSID']}  \n**Password:** {wifi['Password']}")
else:
    st.write("No WiFi profiles found.")

st.write("Note: This application works only on Windows.")

st.info("To use this application, you must have the necessary permissions to access WiFi profiles on your device.")
