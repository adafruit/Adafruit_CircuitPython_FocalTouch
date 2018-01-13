# Simple painting demo

import time
import busio
import board
import digitalio
from ft62xx import adafruit_ft62xx
     
# Create library object using our Bus I2C & SPI port
i2c = busio.I2C(board.SCL, board.SDA)
spi = busio.SPI(clock=board.SCK, MOSI=board.MOSI, MISO=board.MISO)

# Adafruit Metro M0 + 2.8" Capacitive touch shield
cs_pin = digitalio.DigitalInOut(board.D10)
dc_pin = digitalio.DigitalInOut(board.D9)

# Initialize display
from adafruit_rgb_display import ili9341, color565
display = ili9341.ILI9341(spi, cs=cs_pin, dc=dc_pin)
# Fill with black!
display.fill(color565(0, 0, 0))

ft = adafruit_ft62xx.Adafruit_FT6206(i2c)

while True:
    if ft.touched:
        ts = ft.touches
        point = ts[0]   # the shield only supports one point!
        # perform transformation to get into display coordinate system!
        y = 320 - point['y']
        x = 240 - point['x']
        display.fill_rectangle(x-2, y-2, 4, 4, color565(255, 255, 255))
