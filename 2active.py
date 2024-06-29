import subprocess

def get_active_wifi_networks():
    # Get the list of all active WiFi networks
    networks_data = subprocess.check_output(['netsh', 'wlan', 'show', 'network', 'mode=Bssid']).decode('utf-8', errors='ignore').split('\n')
    
    networks = []
    network = {}
    
    for line in networks_data:
        line = line.strip()
        if line.startswith("SSID"):
            if network:
                networks.append(network)
                network = {}
            network['SSID'] = line.split(":")[1].strip()
        elif line.startswith("Signal"):
            network['Signal'] = line.split(":")[1].strip()
        elif line.startswith("BSSID"):
            network['BSSID'] = line.split(":")[1].strip()
        elif line.startswith("Authentication"):
            network['Authentication'] = line.split(":")[1].strip()
        elif line.startswith("Encryption"):
            network['Encryption'] = line.split(":")[1].strip()

    if network:
        networks.append(network)

    return networks

# Get active WiFi networks and print them
active_networks = get_active_wifi_networks()
for network in active_networks:
    print(f"SSID: {network['SSID']}, Signal: {network['Signal']}, BSSID: {network['BSSID']}, Authentication: {network['Authentication']}, Encryption: {network['Encryption']}")
