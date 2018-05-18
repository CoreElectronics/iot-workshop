# We've used 'time' and 'pycom' before. Now we need to use 'machine'
# to read the voltage on one of the pins.
import time
import pycom
import machine

# Stop doing the blue "flash" every 4 seconds.
pycom.heartbeat(False)

# Give it a little bit of time to finish doing the last thing before
# we give it another thing to do
time.sleep(0.1)

# Now set the colour of the light to blue.
# This uses an "RGB" colour code. Learn about RGB here:
# https://www.w3schools.com/colors/colors_rgb.asp
pycom.rgbled(0x0000FF)

# Now we need to use the ADC: Analogue to Digital Converter to
# measure a voltage.

# Here we use the 'machine' library to communicate with the ADC
# part of the device. Created an object called 'adc'
adc = machine.ADC()

# Now we'll tell the 'adc' we want to look at a particular pin,
# a place where we can connect a circuit to the device.
# We're using 'P13'. See where P13 is on the diagram:
# https://docs.pycom.io/chapter/datasheets/downloads/wipy3-pinout.pdf
pin13 = adc.channel(pin='P13', attn=machine.ADC.ATTN_11DB)

# Now we'll tell the device to repeat the rest of the program over and over
while(True):

    # pin13() reads the light. If we subtract that from 4095, we
    # get a number that INCREASES as light increase.
    light = 4095 - pin13()

    # Display the light as text on the screen.
    print("Light level: {}".format(light))

    # Make the light level into a colour
    # The colour will be blue, but the brightness will vary.
    colour = int(light / 16)

    # Make the LED on the device change brightness with the photocell.
    pycom.rgbled(colour)

    # This slows things down a bit.
    time.sleep(0.1)
