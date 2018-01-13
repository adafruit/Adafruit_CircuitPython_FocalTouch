import time
import busio
import board
import adafruit_ft62xx

# Create library object using our Bus I2C port
i2c = busio.I2C(board.SCL, board.SDA)

ft = adafruit_ft62xx.Adafruit_FT6206(i2c, debug=False)

while True:
    n = ft.touched
    if n:
        print(ft.touches)
