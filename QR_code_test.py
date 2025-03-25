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
gImage_custom = [0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x80, 0x00, 0x00, 0x3c, 0x7c, 0x00, 0x1f, 0xf0, 
0x00, 0x07, 0xf8, 0xff, 0x00, 0x00, 0x00, 0x7f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x00, 0x00, 0x00, 0x3c, 0x78, 0x00, 0x0f, 0xe0, 
0x00, 0x03, 0xf8, 0x7f, 0x00, 0x00, 0x00, 0x3f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x00, 0x00, 0x00, 0x3c, 0x78, 0x00, 0x0f, 0xe0, 
0x00, 0x03, 0xf8, 0x7f, 0x00, 0x00, 0x00, 0x3f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x00, 0x00, 0x00, 0x3c, 0x78, 0x00, 0x0f, 0xe0, 
0x00, 0x03, 0xf8, 0x7f, 0x00, 0x00, 0x00, 0x3f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x0f, 0xff, 0xfc, 0x3c, 0x7f, 0x87, 0x0f, 0xe1, 
0xc3, 0xfc, 0x00, 0x0f, 0x0f, 0xff, 0xfc, 0x3f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x0f, 0xff, 0xfc, 0x3c, 0x7f, 0x8f, 0x0f, 0xe1, 
0xe3, 0xfc, 0x00, 0x0f, 0x0f, 0xff, 0xfc, 0x3f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x0f, 0xff, 0xfc, 0x3c, 0x7f, 0x8f, 0x0f, 0xe1, 
0xe3, 0xfc, 0x00, 0x0f, 0x0f, 0xff, 0xfc, 0x3f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x0f, 0xff, 0xfc, 0x3c, 0x7f, 0x8f, 0x0f, 0xe1, 
0xe3, 0xfc, 0x00, 0x0f, 0x0f, 0xff, 0xfc, 0x3f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x0f, 0x00, 0x1c, 0x3f, 0xf8, 0x0f, 0xff, 0xfe, 
0x1f, 0xfc, 0x07, 0x8f, 0x0e, 0x00, 0x3c, 0x3f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x0f, 0x00, 0x1c, 0x3f, 0xf8, 0x0f, 0xff, 0xfe, 
0x1f, 0xfc, 0x07, 0x8f, 0x0e, 0x00, 0x3c, 0x3f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x0f, 0x00, 0x1c, 0x3f, 0xf8, 0x0f, 0xff, 0xfe, 
0x1f, 0xfc, 0x07, 0x8f, 0x0e, 0x00, 0x3c, 0x3f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x0f, 0x00, 0x1c, 0x3c, 0x7c, 0x0f, 0xf1, 0xf0, 
0x3f, 0xc0, 0x07, 0x8f, 0x0e, 0x00, 0x3c, 0x3f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x0f, 0x00, 0x1c, 0x3c, 0x7f, 0xff, 0xf1, 0xe1, 
0xff, 0xc0, 0x07, 0x8f, 0x0e, 0x00, 0x3c, 0x3f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x0f, 0x00, 0x1c, 0x3c, 0x7f, 0xff, 0xf1, 0xe1, 
0xff, 0xc0, 0x07, 0x8f, 0x0e, 0x00, 0x3c, 0x3f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x0f, 0x00, 0x1c, 0x3c, 0x7f, 0xff, 0xf1, 0xe1, 
0xff, 0xc0, 0x07, 0x8f, 0x0e, 0x00, 0x3c, 0x3f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x0f, 0x00, 0x1c, 0x3f, 0x87, 0x8f, 0xf1, 0xff, 
0xff, 0xc0, 0x78, 0x7f, 0x0e, 0x00, 0x3c, 0x3f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x0f, 0x00, 0x1c, 0x3f, 0x87, 0x8f, 0xf1, 0xff, 
0xff, 0xc0, 0x78, 0x7f, 0x0e, 0x00, 0x3c, 0x3f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x0f, 0x00, 0x1c, 0x3f, 0x87, 0x8f, 0xf1, 0xff, 
0xff, 0xc0, 0x78, 0x7f, 0x0e, 0x00, 0x3c, 0x3f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x0f, 0x00, 0x1c, 0x3f, 0xc7, 0x8f, 0xf1, 0xff, 
0xff, 0xc0, 0x78, 0x7f, 0x0e, 0x00, 0x3c, 0x3f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x0f, 0xff, 0xfc, 0x3f, 0xf8, 0x70, 0x0f, 0xfe, 
0x00, 0x03, 0xff, 0x8f, 0x0f, 0xff, 0xfc, 0x3f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x0f, 0xff, 0xfc, 0x3f, 0xf8, 0x70, 0x0f, 0xfe, 
0x00, 0x03, 0xff, 0x8f, 0x0f, 0xff, 0xfc, 0x3f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x0f, 0xff, 0xfc, 0x3f, 0xf8, 0x70, 0x0f, 0xfe, 
0x00, 0x03, 0xff, 0x8f, 0x0f, 0xff, 0xfc, 0x3f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x00, 0x00, 0x00, 0x3c, 0x78, 0x70, 0x01, 0xf0, 
0x00, 0x03, 0xcf, 0x8f, 0x00, 0x00, 0x00, 0x3f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x00, 0x00, 0x00, 0x3c, 0x78, 0x70, 0xf1, 0xe1, 
0xe3, 0xc3, 0x87, 0x8f, 0x00, 0x00, 0x00, 0x3f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x00, 0x00, 0x00, 0x3c, 0x78, 0x70, 0xf1, 0xe1, 
0xe3, 0xc3, 0x87, 0x8f, 0x00, 0x00, 0x00, 0x3f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x00, 0x00, 0x00, 0x3c, 0x78, 0x70, 0xf1, 0xe1, 
0xe3, 0xc3, 0x87, 0x8f, 0x00, 0x00, 0x00, 0x3f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xfc, 0x78, 0x7f, 0xff, 0xfe, 
0x03, 0xc3, 0x80, 0x7f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xfc, 0x78, 0x7f, 0xff, 0xfe, 
0x03, 0xc3, 0x80, 0x7f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xfc, 0x78, 0x7f, 0xff, 0xfe, 
0x03, 0xc3, 0x80, 0x7f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xfc, 0x78, 0x7f, 0xff, 0xfe, 
0x03, 0xc3, 0x80, 0x7f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x0f, 0x01, 0xe0, 0x03, 0x87, 0x80, 0xf1, 0xe0, 
0x00, 0x3c, 0x78, 0x0f, 0x0f, 0xe1, 0xc0, 0x3f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x0f, 0x01, 0xe0, 0x03, 0x87, 0x80, 0xf1, 0xe0, 
0x00, 0x3c, 0x78, 0x0f, 0x0f, 0xe1, 0xc0, 0x3f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x0f, 0x01, 0xe0, 0x03, 0x87, 0x80, 0xf1, 0xe0, 
0x00, 0x3c, 0x78, 0x0f, 0x0f, 0xe1, 0xc0, 0x3f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x8f, 0x01, 0xe0, 0x07, 0xc7, 0x80, 0xf1, 0xe0, 
0x00, 0x00, 0x78, 0x0f, 0x01, 0xe0, 0x00, 0x3f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x1f, 0xe3, 0xff, 0xff, 0xff, 0xff, 0xe1, 
0xe0, 0x00, 0x78, 0x7f, 0x01, 0xe0, 0x00, 0x3f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x1f, 0xe3, 0xff, 0xff, 0xff, 0xff, 0xe1, 
0xe0, 0x00, 0x78, 0x7f, 0x01, 0xe0, 0x00, 0x3f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x1f, 0xe3, 0xff, 0xff, 0xff, 0xff, 0xe1, 
0xe0, 0x00, 0x78, 0x7f, 0x01, 0xe0, 0x00, 0x3f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xe0, 0x00, 0x03, 0xc0, 0x0f, 0xf1, 0xe0, 
0x1f, 0xff, 0xf8, 0x70, 0xe0, 0x01, 0xc0, 0x3f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xe0, 0x00, 0x03, 0x80, 0x0f, 0xf1, 0xe0, 
0x1f, 0xff, 0xf8, 0x70, 0xf0, 0x01, 0xc0, 0x3f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xe0, 0x00, 0x03, 0x80, 0x0f, 0xf1, 0xe0, 
0x1f, 0xff, 0xf8, 0x70, 0xf0, 0x01, 0xc0, 0x3f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xe0, 0x00, 0x03, 0xc0, 0x07, 0xf0, 0xe0, 
0x1f, 0xff, 0xf8, 0x70, 0xf0, 0x01, 0xc0, 0x3f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xf0, 0xff, 0xff, 0xff, 0xff, 0x80, 0x00, 0x1f, 
0xe3, 0xc3, 0xf8, 0x0f, 0xf1, 0xe1, 0xc0, 0x3f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xf0, 0xff, 0xff, 0xff, 0xff, 0x80, 0x00, 0x1f, 
0xe3, 0xc3, 0xf8, 0x0f, 0xf1, 0xe1, 0xc0, 0x3f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xf0, 0xff, 0xff, 0xff, 0xff, 0x80, 0x00, 0x1f, 
0xe3, 0xc3, 0xf8, 0x0f, 0xf1, 0xe1, 0xc0, 0x3f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xf9, 0xf1, 0xe0, 0x3f, 0xc7, 0x80, 0x00, 0x1f, 
0xe0, 0x00, 0x78, 0x01, 0xf0, 0x01, 0xe0, 0x7f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xe1, 0xe0, 0x3f, 0x87, 0xff, 0xff, 0xff, 
0xe0, 0x3c, 0x78, 0x70, 0xf0, 0x01, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xe1, 0xe0, 0x3f, 0x87, 0xff, 0xff, 0xff, 
0xe0, 0x3c, 0x78, 0x70, 0xf0, 0x01, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xe1, 0xe0, 0x3f, 0x87, 0xff, 0xff, 0xff, 
0xe0, 0x3c, 0x78, 0x70, 0xf0, 0x01, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x80, 0x01, 0xe1, 0xff, 0x80, 0x78, 0xff, 0xe1, 
0xe3, 0xfc, 0x07, 0x8f, 0xf1, 0xe1, 0xc3, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x00, 0x01, 0xe3, 0xff, 0x80, 0x70, 0xff, 0xe1, 
0xe3, 0xfc, 0x07, 0x8f, 0xf1, 0xe1, 0xc3, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x00, 0x01, 0xe3, 0xff, 0x80, 0x70, 0xff, 0xe1, 
0xe3, 0xfc, 0x07, 0x8f, 0xf1, 0xe1, 0xc3, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x00, 0x01, 0xe3, 0xff, 0x80, 0x78, 0xff, 0xe1, 
0xe3, 0xfc, 0x07, 0x8f, 0xf1, 0xe1, 0xc3, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xe1, 0xe0, 0x00, 0x00, 0x7f, 0x00, 0x01, 
0xe3, 0xfc, 0x7f, 0xff, 0x00, 0x00, 0x3f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xe1, 0xe0, 0x00, 0x00, 0x7f, 0x00, 0x01, 
0xe3, 0xfc, 0x7f, 0xff, 0x00, 0x00, 0x3f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xe1, 0xe0, 0x00, 0x00, 0x7f, 0x00, 0x01, 
0xe3, 0xfc, 0x7f, 0xff, 0x00, 0x00, 0x3f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xe1, 0xe0, 0x00, 0x00, 0xff, 0x00, 0x01, 
0xe3, 0xf8, 0x7f, 0xff, 0x00, 0x00, 0x3f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x00, 0x01, 0xff, 0xc3, 0x87, 0xf0, 0x0f, 0xe1, 
0xe0, 0x00, 0x78, 0x00, 0x0f, 0xfe, 0x3f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x00, 0x01, 0xff, 0xc3, 0x87, 0xf0, 0x0f, 0xe1, 
0xe0, 0x00, 0x78, 0x00, 0x0f, 0xfe, 0x3f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x00, 0x01, 0xff, 0xc3, 0x87, 0xf0, 0x0f, 0xe1, 
0xe0, 0x00, 0x78, 0x00, 0x0f, 0xfe, 0x3f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xf0, 0x01, 0xfe, 0x3c, 0x07, 0x80, 0x0f, 0x1f, 
0xe0, 0x00, 0x78, 0x70, 0x0e, 0x00, 0x3f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xf0, 0x01, 0xfc, 0x3c, 0x07, 0x80, 0x0e, 0x1f, 
0xe0, 0x00, 0x78, 0x70, 0x0e, 0x00, 0x3f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xf0, 0x01, 0xfc, 0x3c, 0x07, 0x80, 0x0e, 0x1f, 
0xe0, 0x00, 0x78, 0x70, 0x0e, 0x00, 0x3f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xf0, 0x01, 0xfc, 0x3c, 0x07, 0x80, 0x0e, 0x1f, 
0xe0, 0x00, 0x78, 0x70, 0x0e, 0x00, 0x3f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xfe, 0x03, 0xff, 0x80, 0x00, 0x00, 0x00, 
0x1f, 0xfc, 0x00, 0x70, 0x0e, 0x01, 0xfc, 0x3f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xfe, 0x03, 0xff, 0x80, 0x00, 0x00, 0x00, 
0x1f, 0xfc, 0x00, 0x70, 0x0e, 0x01, 0xfc, 0x3f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xfe, 0x03, 0xff, 0x80, 0x00, 0x00, 0x00, 
0x1f, 0xfc, 0x00, 0x70, 0x0e, 0x01, 0xfc, 0x3f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xfe, 0x03, 0xff, 0x80, 0x00, 0x00, 0x00, 
0x1f, 0xfc, 0x00, 0xf8, 0x0e, 0x01, 0xfc, 0x7f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x00, 0x1c, 0x03, 0x80, 0x7f, 0xfe, 0x00, 
0x1f, 0xc3, 0x87, 0xff, 0x00, 0x1e, 0x03, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x00, 0x1c, 0x03, 0x80, 0x7f, 0xfe, 0x00, 
0x1f, 0xc3, 0x87, 0xff, 0x00, 0x1e, 0x03, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x00, 0x1c, 0x03, 0x80, 0x7f, 0xfe, 0x00, 
0x1f, 0xc3, 0x87, 0xff, 0x00, 0x1e, 0x03, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xe1, 0xe3, 0xc0, 0x7f, 0x8f, 0xf1, 0xe1, 
0xff, 0xfc, 0x78, 0x00, 0x0e, 0x1f, 0xc3, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xe1, 0xe3, 0xc0, 0x7f, 0x8f, 0xf1, 0xe1, 
0xff, 0xfc, 0x78, 0x00, 0x0e, 0x1f, 0xc3, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xe1, 0xe3, 0xc0, 0x7f, 0x8f, 0xf1, 0xe1, 
0xff, 0xfc, 0x78, 0x00, 0x0e, 0x1f, 0xc3, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xe1, 0xe3, 0xc0, 0x7f, 0x8f, 0xf1, 0xe1, 
0xff, 0xfc, 0x78, 0x00, 0x0e, 0x1f, 0xc3, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x00, 0xff, 0xfc, 0x00, 0x00, 0x70, 0x0f, 0xff, 
0xe0, 0x03, 0xff, 0x8f, 0xff, 0xe0, 0x3c, 0x3f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x00, 0xff, 0xfc, 0x00, 0x00, 0x70, 0x0f, 0xff, 
0xe0, 0x03, 0xff, 0x8f, 0xff, 0xe0, 0x3c, 0x3f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x00, 0xff, 0xfc, 0x00, 0x00, 0x70, 0x0f, 0xff, 
0xe0, 0x03, 0xff, 0x8f, 0xff, 0xe0, 0x3c, 0x3f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x00, 0xff, 0xfe, 0x00, 0x00, 0x70, 0x0f, 0xff, 
0xc0, 0x07, 0xff, 0x8f, 0xff, 0xe0, 0x3c, 0x3f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x00, 0xfe, 0x1f, 0xc0, 0x78, 0x00, 0x00, 0x1e, 
0x03, 0xff, 0xf8, 0x70, 0x0f, 0xe1, 0xfc, 0x3f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x00, 0xfe, 0x1f, 0xc0, 0x78, 0x00, 0x00, 0x1e, 
0x03, 0xff, 0xf8, 0x70, 0x0f, 0xe1, 0xfc, 0x3f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x00, 0xfe, 0x1f, 0xc0, 0x78, 0x00, 0x00, 0x1e, 
0x03, 0xff, 0xf8, 0x70, 0x0f, 0xe1, 0xfc, 0x3f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x1e, 0x00, 0x38, 0x00, 0x07, 0x0f, 0xe0, 
0x03, 0xfc, 0x00, 0x7f, 0x0f, 0xfe, 0x00, 0x3f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x1e, 0x00, 0x3c, 0x00, 0x0f, 0x0f, 0xe0, 
0x03, 0xfc, 0x00, 0x7f, 0x0f, 0xfe, 0x00, 0x3f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x1e, 0x00, 0x3c, 0x00, 0x0f, 0x0f, 0xe0, 
0x03, 0xfc, 0x00, 0x7f, 0x0f, 0xfe, 0x00, 0x3f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x1e, 0x00, 0x3c, 0x00, 0x0f, 0x0f, 0xe0, 
0x03, 0xfc, 0x00, 0x7f, 0x0f, 0xfe, 0x00, 0x3f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xf0, 0xff, 0xe3, 0xfc, 0x7f, 0x8f, 0xff, 0xe1, 
0xfc, 0x3f, 0x87, 0x8f, 0x0f, 0xe1, 0xc3, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xf0, 0xff, 0xe3, 0xfc, 0x7f, 0x8f, 0xff, 0xe1, 
0xfc, 0x3f, 0x87, 0x8f, 0x0f, 0xe1, 0xc3, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xf0, 0xff, 0xe3, 0xfc, 0x7f, 0x8f, 0xff, 0xe1, 
0xfc, 0x3f, 0x87, 0x8f, 0x0f, 0xe1, 0xc3, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xf0, 0xff, 0xe3, 0xfc, 0x3f, 0x8f, 0xff, 0xe1, 
0xfc, 0x3f, 0x87, 0x87, 0x0f, 0xe3, 0xc3, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x0f, 0x01, 0xfc, 0x3c, 0x07, 0x8f, 0xf0, 0x1e, 
0x1f, 0xc3, 0x87, 0x80, 0x00, 0x1f, 0xc0, 0x3f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x0f, 0x01, 0xfc, 0x3c, 0x07, 0x8f, 0xf0, 0x1e, 
0x1f, 0xc3, 0x87, 0x80, 0x00, 0x1f, 0xc0, 0x3f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x0f, 0x01, 0xfc, 0x3c, 0x07, 0x8f, 0xf0, 0x1e, 
0x1f, 0xc3, 0x87, 0x80, 0x00, 0x1f, 0xc0, 0x3f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xfc, 0x00, 0x7f, 0xf0, 0x00, 
0x1c, 0x3f, 0xf8, 0x07, 0xfe, 0x03, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xfc, 0x00, 0x7f, 0xf0, 0x00, 
0x1c, 0x3f, 0xf8, 0x0f, 0xfe, 0x01, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xfc, 0x00, 0x7f, 0xf0, 0x00, 
0x1c, 0x3f, 0xf8, 0x0f, 0xfe, 0x01, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xfc, 0x00, 0x7f, 0xf0, 0x00, 
0x1c, 0x3f, 0xf8, 0x0f, 0xfe, 0x01, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x00, 0x00, 0x00, 0x3c, 0x07, 0x80, 0x0f, 0xff, 
0xfc, 0x3f, 0x80, 0x0f, 0x0e, 0x1f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x00, 0x00, 0x00, 0x3c, 0x07, 0x80, 0x0f, 0xff, 
0xfc, 0x3f, 0x80, 0x0f, 0x0e, 0x1f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x00, 0x00, 0x00, 0x3c, 0x07, 0x80, 0x0f, 0xff, 
0xfc, 0x3f, 0x80, 0x0f, 0x0e, 0x1f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x00, 0x00, 0x00, 0x3c, 0x07, 0x80, 0x0f, 0xff, 
0xfc, 0x3f, 0x80, 0x0f, 0x1e, 0x1f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x0f, 0xff, 0xfc, 0x3c, 0x7f, 0x80, 0x0f, 0xe1, 
0xff, 0xc0, 0x00, 0x0f, 0xfe, 0x00, 0x3c, 0x3f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x0f, 0xff, 0xfc, 0x3c, 0x7f, 0x80, 0x0f, 0xe1, 
0xff, 0xc0, 0x00, 0x0f, 0xfe, 0x00, 0x3c, 0x3f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x0f, 0xff, 0xfc, 0x3c, 0x7f, 0x80, 0x0f, 0xe1, 
0xff, 0xc0, 0x00, 0x0f, 0xfe, 0x00, 0x3c, 0x3f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x0f, 0x00, 0x3c, 0x3f, 0xf8, 0x00, 0xf1, 0xfe, 
0x3f, 0xc3, 0xf8, 0x00, 0x00, 0x1c, 0x3f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x0f, 0x00, 0x1c, 0x3f, 0xf8, 0x00, 0xf1, 0xfe, 
0x1f, 0xc3, 0xf8, 0x00, 0x00, 0x1e, 0x3f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x0f, 0x00, 0x1c, 0x3f, 0xf8, 0x00, 0xf1, 0xfe, 
0x1f, 0xc3, 0xf8, 0x00, 0x00, 0x1e, 0x3f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x0f, 0x00, 0x1c, 0x3f, 0xf8, 0x00, 0xf1, 0xfe, 
0x1f, 0xc3, 0xf8, 0x00, 0x00, 0x1e, 0x3f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x0f, 0x00, 0x1c, 0x3c, 0x78, 0x0f, 0xf1, 0xff, 
0xe0, 0x03, 0xf8, 0x0f, 0xf1, 0xff, 0xc0, 0x3f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x0f, 0x00, 0x1c, 0x3c, 0x78, 0x0f, 0xf1, 0xff, 
0xe0, 0x03, 0xf8, 0x0f, 0xf1, 0xff, 0xc0, 0x3f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x0f, 0x00, 0x1c, 0x3c, 0x78, 0x0f, 0xf1, 0xff, 
0xe0, 0x03, 0xf8, 0x0f, 0xf1, 0xff, 0xc0, 0x3f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x0f, 0x00, 0x1c, 0x3c, 0x38, 0x0f, 0xf1, 0xff, 
0xe0, 0x03, 0xf8, 0x0f, 0xe1, 0xff, 0xc0, 0x7f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x0f, 0x00, 0x1c, 0x3c, 0x07, 0xf0, 0x01, 0xff, 
0xfc, 0x3c, 0x07, 0x80, 0x01, 0xe1, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x0f, 0x00, 0x1c, 0x3c, 0x07, 0xf0, 0x01, 0xff, 
0xfc, 0x3c, 0x07, 0x80, 0x01, 0xe1, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x0f, 0x00, 0x1c, 0x3c, 0x07, 0xf0, 0x01, 0xff, 
0xfc, 0x3c, 0x07, 0x80, 0x01, 0xe1, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x0f, 0xff, 0xfc, 0x3f, 0xf8, 0xff, 0xf0, 0x00, 
0x00, 0x3f, 0x87, 0x87, 0x00, 0x1f, 0xfc, 0x7f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x0f, 0xff, 0xfc, 0x3f, 0xf8, 0x7f, 0xf0, 0x00, 
0x00, 0x3f, 0x87, 0x8f, 0x00, 0x1f, 0xfc, 0x3f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x0f, 0xff, 0xfc, 0x3f, 0xf8, 0x7f, 0xf0, 0x00, 
0x00, 0x3f, 0x87, 0x8f, 0x00, 0x1f, 0xfc, 0x3f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x0f, 0xff, 0xfc, 0x3f, 0xf8, 0x7f, 0xf0, 0x00, 
0x00, 0x3f, 0x87, 0x8f, 0x00, 0x1f, 0xfc, 0x3f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x00, 0x00, 0x00, 0x3c, 0x00, 0x78, 0xfe, 0x00, 
0x03, 0xfc, 0x78, 0x7f, 0x0e, 0x1e, 0x3f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x00, 0x00, 0x00, 0x3c, 0x00, 0x70, 0xfe, 0x00, 
0x03, 0xfc, 0x78, 0x7f, 0x0e, 0x1e, 0x3f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x00, 0x00, 0x00, 0x3c, 0x00, 0x70, 0xfe, 0x00, 
0x03, 0xfc, 0x78, 0x7f, 0x0e, 0x1e, 0x3f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0, 
0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x80, 0x00, 0x00, 0x3c, 0x00, 0x78, 0xff, 0x00, 
0x03, 0xfc, 0x78, 0xff, 0x1e, 0x1e, 0x3f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xc0]

# Display the image on the e-paper display
gui.epd.whitescreen_all_fast(gImage_custom)
time.sleep(2)  # Pause for 2 seconds to view the image

# Enter deep sleep mode after display (as required by your device)
gui.epd.sleep()

# Clean up GPIO settings before exiting
gui.epd.clean_gpio()
