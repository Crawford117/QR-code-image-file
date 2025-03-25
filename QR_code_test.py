from PIL import Image
import time
from epd_2inch13 import *
from epd_gui import *
import gpiozero

# Set your display dimensions.
EPD_WIDTH = 122
EPD_HEIGHT = 250
gui = EPD_GUI()
# Open your image file using the full file path.
im = Image.open("/home/bruh/Desktop/QR code.bmp")

# Resize the image to the display resolution.
im = im.resize((EPD_WIDTH, EPD_HEIGHT))

# Convert the image to 1-bit (black & white).
im = im.convert("1")

# Get the raw bytes of the image.
raw_bytes = im.tobytes()

# Calculate the expected number of bytes.
# The driver expects 16 bytes per row (since 122 // 8 is 15 and then +1 = 16),
# and 16 bytes * 250 rows = 4000 bytes.
expected_bytes_per_row = (EPD_WIDTH // 8) + 1
expected_total_bytes = expected_bytes_per_row * EPD_HEIGHT

print("Length of raw bytes:", len(raw_bytes))
print("Expected total bytes:", expected_total_bytes)

# If needed, pad the data to reach the expected length.
if len(raw_bytes) < expected_total_bytes:
    pad_length = expected_total_bytes - len(raw_bytes)
    raw_bytes += bytes([0xFF] * pad_length)  # 0xFF is white for 1-bit images.
elif len(raw_bytes) > expected_total_bytes:
    raw_bytes = raw_bytes[:expected_total_bytes]

# Convert to a list of integers for your driver.
gImage_custom = list(raw_bytes)
print("Length of gImage_custom array:", len(gImage_custom))


# Display the image on the e-paper display
gui.epd.whitescreen_all_fast(gImage_custom)
time.sleep(2)  # Pause for 2 seconds to view the image

# Enter deep sleep mode after display (as required by your device)
gui.epd.sleep()

# Clean up GPIO settings before exiting
gui.epd.clean_gpio()
