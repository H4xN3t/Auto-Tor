import time
import requests
import os

# Tor SOCKS5 proxy settings
proxies = {
    'http': 'socks5h://127.0.0.1:9050',
    'https': 'socks5h://127.0.0.1:9050'
}

# Function to check current IP
def get_current_ip():
    try:
        response = requests.get("http://httpbin.org/ip", proxies=proxies, timeout=10)
        return response.json().get("origin")
    except requests.RequestException as e:
        print(f"Error: {e}")
        return None

# Loop to restart Tor and check IP
while True:
    # Restart Tor service to obtain new IP
    print("Restarting Tor for new IP...")
    os.system("pkill tor")  # Stop Tor
    time.sleep(2)            # Wait briefly
    os.system("tor -f ~/.tor/torrc &")  # Restart Tor with config
    
    # Wait a moment for Tor to re-establish connection
    time.sleep(5)
    
    # Get and print the current IP
    current_ip = get_current_ip()
    print(f"Current IP: {current_ip}")
    
    # Wait before restarting again (adjust this delay as needed)
    time.sleep(10)
