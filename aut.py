import time
import requests
from stem import Signal
from stem.control import Controller

# Tor SOCKS5 proxy settings
proxies = {
    'http': 'socks5h://127.0.0.1:9050',
    'https': 'socks5h://127.0.0.1:9050'
}

# Function to request a new Tor circuit
def renew_connection():
    with Controller.from_port(port=9051) as controller:
        controller.authenticate()  # No password needed if CookieAuthentication is off
        controller.signal(Signal.NEWNYM)

# Function to check current IP
def get_current_ip():
    try:
        response = requests.get("http://httpbin.org/ip", proxies=proxies, timeout=10)
        return response.json().get("origin")
    except requests.RequestException as e:
        print(f"Error: {e}")
        return None

# Main loop to change IP every second
while True:
    print("Requesting new IP...")
    renew_connection()
    time.sleep(1)  # Wait a second for the new circuit to establish
    current_ip = get_current_ip()
    print(f"Current IP: {current_ip}")
