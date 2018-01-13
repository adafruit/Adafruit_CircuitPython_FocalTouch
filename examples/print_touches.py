import time
import busio
import board
import adafruit_focaltouch

# Create library object using our Bus I2C port
i2c = busio.I2C(board.SCL, board.SDA)

ft = adafruit_focaltouch.Adafruit_FocalTouch(i2c, debug=True)

while True:
    n = ft.touched
    if n:
        print(ft.touches)
