# import statements allow us to use libraries of code that we didn't create
# We need one for time, so we can tell the device to 'sleep' when
# we need to make it wait for something to happen.
# WLAN means Wireless Local Area Network. We need this to connect
# to any WiFi network
import time
from network import WLAN

# Wireless network settings
# We create variables to store these things so when we need to change them
# we don't have to search through pages of code to find them.
WIFI_NETWORK_NAME = "IoT"
WIFI_PASSWORD = "45GreenCarpet" # No this is not our regular password. :)

# Turn off the heartbeat and change the LED to red.
pycom.heartbeat(False)
time.sleep(0.1)
pycom.rgbled(0xFF0000)

# We need to have a connection to WiFi for Internet access
# Code source: https://docs.pycom.io/chapter/tutorials/all/wlan.html

# Print a message to explain what's happening on the device.
print("Connecting to Wifi ", end='')

# Use the WiFi network's name and password to connect
# Code source: https://docs.pycom.io/chapter/tutorials/all/wlan.html
wlan = WLAN(mode=WLAN.STA)
wlan.connect(WIFI_NETWORK_NAME, auth=(WLAN.WPA2, WIFI_PASSWORD), timeout=5000)

# The 'while' statement makes everything indented below repeat over and
# over until the 'not wlan.isconnected()' part becomes true.
while not wlan.isconnected():

    # Displays a line of dots to show that something's happening
    print('.', end='')

    # Delay between drawing dots
    time.sleep(0.1)

# We can only get here if the WiFi connects. So say it's DONE!
print(" DONE!")

# Display a green light
pycom.rgbled(0x00FF00)
