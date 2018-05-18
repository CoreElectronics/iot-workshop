import time
import machine
import ubinascii
from network import WLAN
from machine import Timer
from umqtt import MQTTClient

# SETTINGS

# YOU NEED TO CHANGE THESE SETTINGS!
AIO_USER = "CoreChris"
AIO_KEY = "7b2d0601a9694589a52fb2d614122cff"

# These settings are ok
WIFI_SSID = "IoT"
WIFI_PASS = "35GreenCarpet" # No this is not our regular password. :)
# WIFI_PASS = "79Password#" # No this is not our regular password. :)

AIO_SERVER = "io.adafruit.com"
AIO_PORT = 1883
AIO_CLIENT_ID = ubinascii.hexlify(machine.unique_id())  # Can be anything
AIO_CONTROL_FEED = AIO_USER + "/feeds/control"
AIO_COLOUR_FEED = AIO_USER + "/feeds/colour"
AIO_LIGHT_FEED = AIO_USER + "/feeds/light"

led_colour = 0xFFFFFF # White

def send_to_aio(feed, value):

    value_string = str(value)
    print("Publishing: {0} to {1} ... ".format(str(value_string), feed), end='')
    try:
        adafruit_io.publish(topic=feed, msg=str(value_string))
        print("DONE")
    except Exception as e:
        print("FAILED")

# Function to respond to messages from Adafruit IO
def sub_cb(topic, msg):          # sub_cb means "callback subroutine"
    global led_colour

    print("io.adafruit.com says: {} {}".format(topic, msg))          # Outputs the message that was received. Debugging use.

    if b'control' in topic:
    # if topic == b'CoreChris/feeds/control':
        if msg == b'ON':
            pycom.rgbled(led_colour)
        else:
            pycom.rgbled(0x000000)

    if b'colour' in topic:
    # if topic == b'CoreChris/feeds/colour':
        led_colour = int(msg[1:], 16)
        pycom.rgbled(led_colour)

pycom.heartbeat(False)
adc = machine.ADC()             # create an ADC object
apin = adc.channel(pin='P13')   # create an analog pin on P16

# CONNECT TO WIFI
# We need to have a connection to WiFi for Internet access
# Code source: https://docs.pycom.io/chapter/tutorials/all/wlan.html

print("Connecting to WiFi ... ", end='')
wlan = WLAN(mode=WLAN.STA)
wlan.connect(WIFI_SSID, auth=(WLAN.WPA2, WIFI_PASS), timeout=5000)

while not wlan.isconnected():    # Code waits here until WiFi connects
    machine.idle()

print("done.")

# CONNECT TO ADAFRUIT IO
# Use the MQTT protocol to connect to Adafruit IO
adafruit_io = MQTTClient(AIO_CLIENT_ID, AIO_SERVER, AIO_PORT, AIO_USER, AIO_KEY)
adafruit_io.set_callback(sub_cb)
adafruit_io.connect()
adafruit_io.subscribe(AIO_CONTROL_FEED)
adafruit_io.subscribe(AIO_COLOUR_FEED)

while(True):
    light_level = 4095 - apin()

    send_to_aio(AIO_LIGHT_FEED, light_level)
    for x in range(0,49):
        adafruit_io.check_msg()
        time.sleep(0.1)
