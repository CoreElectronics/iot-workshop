# We need to add the circuit shown on the screen for this to work.

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
apin = adc.channel(pin='P13', attn=machine.ADC.ATTN_11DB)

# Now when the program runs, the device "looks" at pin 13, measures the
# voltage, and gives us a number between zero and 4096.
print("Light level: {}".format(apin()))

# What do you notice about the number? Run the program multiple times
# with different levels of light on the photocell.
