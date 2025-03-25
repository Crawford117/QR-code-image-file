from PIL import Image
import time
from epd_2inch13 import *
from epd_gui import *
import gpiozero

# Create the GUI object
gui = EPD_GUI()

# Initialize the e-paper display quickly
gui.epd.hw_init_fast()

# Define the path to your BMP file on the Desktop
image_path = "/home/pi/Desktop/QR code.bmp"

# Open the BMP image file using PIL
img = Image.open(image_path)

# Convert the image to 1-bit color (black and white) for the e-paper display
img = img.convert("1")

# Optionally, resize the image to match your display resolution if necessary.
# For example, if your display uses 122x250 pixels:
img = img.resize((122, 250), Image.ANTIALIAS)

# Display the image on the e-paper display
gui.epd.display(img)
time.sleep(2)  # Pause for 2 seconds to view the image

# Enter deep sleep mode after display (as required by your device)
gui.epd.sleep()

# Clean up GPIO settings before exiting
gui.epd.clean_gpio()
