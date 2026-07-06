import os
import time
import board
import busio
from Adafruit_IO import Client
import adafruit_ssd1306

from keys.py import username
from keys.py import key

# --- Adafruit IO Setup ---
ADAFRUIT_IO_USERNAME = os.getenv('ADAFRUIT_IO_USERNAME', username)
ADAFRUIT_IO_KEY = os.getenv('ADAFRUIT_IO_KEY', key)

if ADAFRUIT_IO_USERNAME == '"""USER"""' or ADAFRUIT_IO_KEY == '"""key"""':
    raise ValueError("Please set your ADAFRUIT_IO_USERNAME and ADAFRUIT_IO_KEY.")

aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

# --- OLED Display Setup (I2C) ---
# Define I2C interface
i2c = busio.I2C(board.SCL, board.SDA)

# Initialize SSD1306 OLED (128x64 resolution)
# If your screen is 128x32, change the dimensions below
display = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3C)

# Clear display
display.fill(0)
display.show()

try:
    while True:
        # 1. get text (ex:time) #TODO: change display to smt else/ write another file with commands?
        t = aio.receive_time()
        time_str = f"{t.tm_hour:02d}:{t.tm_min:02d}"
        date_str = f"{t.tm_mon}/{t.tm_mday}"

        print(f"Time: {time_str}")

        # 2. Draw to OLED
        display.fill(0)  # Clear buffer

        # Draw Time (Large font simulation by doubling size if supported, or just standard text)
        display.text("Time:", 0, 0, 1)
        display.text(time_str, 0, 10, 1)

        # Draw Date
        display.text("Date:", 0, 30, 1)
        display.text(date_str, 0, 40, 1)

        # 3. Update Screen
        display.show()

        time.sleep(1)

except KeyboardInterrupt:
    print("Exiting...")
except Exception as e:
    print(f"Error: {e}")
    print("Tip: Check wiring and ensure I2C is enabled (sudo raspi-config)")
