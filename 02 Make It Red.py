# 'import' statements allow us to use libraries of code that we didn't create
# We need one for 'time', so we can tell the device to 'sleep' when
# we need to it to wait for something to happen.
# The one called 'pycom' lets us do thing with our Pycom device.
import time
import pycom

# Pycom devices all have a multicoloured light on them, called the RGB LED.
# When the device starts up, it gives blue flash every 4 seconds, called
# the "heartbeat". If we want to use the RGB LED to display a colour,
# we first need to turn off the heartbeat.
pycom.heartbeat(False)

# Give it a little bit of time to finish doing the last thing before
# we give it another thing to do
time.sleep(0.1)

# Now set the colour of the light to blue.
# This uses an "RGB" colour code. Learn about RGB here:
# https://www.w3schools.com/colors/colors_rgb.asp
# Get colour codes from Google: https://www.google.com/search?q=rgb+to+hex&ie=utf-8&oe=utf-8&client=firefox-b-ab

pycom.rgbled(0x0000FF)

# Display a message on the screen to say what should have happened.
print("LED should be BLUE!")

# The program ends here because there's no more
# code to tell it what to do next.
