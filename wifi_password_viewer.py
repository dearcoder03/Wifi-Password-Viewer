import subprocess
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def get_wifi_passwords():
    profiles_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors='ignore').split('\n')
    profiles = [line.split(":")[1][1:-1] for line in profiles_data if "All User Profile" in line]

    wifi_passwords = []

    for profile in profiles:
        profile_info = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', profile, 'key=clear']).decode('utf-8', errors='ignore').split('\n')
        password = None
        auth_type = None
        encryption = None
        for line in profile_info:
            if "Key Content" in line:
                password = line.split(":")[1][1:-1]
            elif "Authentication" in line:
                auth_type = line.split(":")[1][1:-1]
            elif "Cipher" in line:
                encryption = line.split(":")[1][1:-1]
        wifi_passwords.append({'SSID': profile, 'Password': password, 'Authentication': auth_type, 'Encryption': encryption})

    return wifi_passwords

# Streamlit app
st.title("WiFi Password Viewer")

st.write("This application will show you the SSID and passwords of all saved WiFi profiles on your device.")

passwords = get_wifi_passwords()

# Filter and Search
filter_option = st.selectbox("Filter by:", ["All", "Most Recently Used", "Password Available"])
search = st.text_input("Search for a specific SSID:")

if filter_option == "Most Recently Used":
    passwords = sorted(passwords, key=lambda x: x['SSID'], reverse=True)
elif filter_option == "Password Available":
    passwords = [wifi for wifi in passwords if wifi['Password']]

if search:
    passwords = [wifi for wifi in passwords if search.lower() in wifi['SSID'].lower()]

if passwords:
    df = pd.DataFrame(passwords)
    st.dataframe(df)

    # Export to file
    csv = df.to_csv(index=False)
    st.download_button(label="Download data as CSV", data=csv, file_name='wifi_passwords.csv', mime='text/csv')

    # Graphical visualization
    st.write("### Most Frequently Connected Networks")
    ssid_counts = df['SSID'].value_counts()
    fig, ax = plt.subplots()
    ssid_counts.plot(kind='bar', ax=ax)
    st.pyplot(fig)

    for wifi in passwords:
        st.write(f"**SSID:** {wifi['SSID']}  \n**Password:** {wifi['Password']}  \n**Authentication:** {wifi['Authentication']}  \n**Encryption:** {wifi['Encryption']}")
else:
    st.write("No WiFi profiles found.")

st.write("Note: This application works only on Windows.")

st.info("To use this application, you must have the necessary permissions to access WiFi profiles on your device.")
