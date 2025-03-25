#!/usr/bin/env python3
import os
import sys
import time
import numpy as np
from epd_2inch13 import EPD_2Inch13  # This is your driver file.
from PIL import Image, ImageFont
from gpiozero import *

#----------------------------
# Constants & Definitions
#----------------------------
FILL_EMPTY = 0
FILL_FULL = 1

LINE_SOLID = 0
LINE_DOTTED = 1
FONT_SIZE_16 = 16
FONT_SIZE_20 = 20
FONT_SIZE_24 = 24
FONT_SIZE_28 = 28

PIXEL_1X1 = 1  # 1x1
PIXEL_2X2 = 2
PIXEL_3X3 = 3
PIXEL_4X4 = 4
PIXEL_5X5 = 5
PIXEL_6X6 = 6
PIXEL_7X7 = 7
PIXEL_8X8 = 8
DOT_PIXEL_DFT = PIXEL_1X1  # Default dot style

WHITE = 0xFF
BLACK = 0x00
RED = BLACK
IMAGE_BACKGROUND = WHITE
FONT_FOREGROUND = BLACK
FONT_BACKGROUND = WHITE

MIRROR_NONE = 0x00
MIRROR_HORIZONTAL = 0x01
MIRROR_VERTICAL = 0x02
MIRROR_ORIGIN = 0x03

ROTATE_0 = 0
ROTATE_90 = 90
ROTATE_180 = 180
ROTATE_270 = 270

AROUND = 1  # dot pixel 1x1
RIGHTUP = 2  # dot pixel 2x2
DOT_STYLE_DFT = AROUND

EPD_WIDTH  = 122
EPD_HEIGHT = 250

#----------------------------
# EPD_GUI Class Definition
#----------------------------
class EPD_GUI():
    def __init__(self):
        self.epd = EPD_2Inch13()
        self.epd.reset()
        self.epd.hw_init()
        # Create an image buffer (filled with white)
        self.img = [0xff for i in range(4000)]
        self.mem_w = EPD_WIDTH
        self.mem_h = EPD_HEIGHT
        self.color = WHITE
        self.rotate = ROTATE_0
        self.mirror = MIRROR_HORIZONTAL
        if EPD_WIDTH % 8 == 0:
            self.byte_w = EPD_WIDTH // 8
        else:
            self.byte_w = (EPD_WIDTH // 8) + 1
        self.byte_h = EPD_HEIGHT
        if self.rotate == ROTATE_0 or self.rotate == ROTATE_180:
            self.w = EPD_WIDTH
            self.h = EPD_HEIGHT
        else:
            self.w = EPD_HEIGHT
            self.h = EPD_WIDTH

    def set_pixel(self, x, y, color):
        if x >= self.w or y >= self.h:
            # Outside display range.
            return
        # Adjust coordinates for rotation.
        if self.rotate == ROTATE_0:
            xx = x
            yy = y
        elif self.rotate == ROTATE_90:
            xx = self.mem_w - y - 1
            yy = x
        elif self.rotate == ROTATE_180:
            xx = self.mem_w - x - 1
            yy = self.mem_h - y - 1
        elif self.rotate == ROTATE_270:
            xx = y
            yy = self.mem_h - x - 1
        else:
            xx = x
            yy = y

        # Apply mirror settings.
        if self.mirror == MIRROR_HORIZONTAL:
            xx = self.mem_w - xx - 1
        elif self.mirror == MIRROR_VERTICAL:
            yy = self.mem_h - yy - 1
        elif self.mirror == MIRROR_ORIGIN:
            xx = self.mem_w - xx - 1
            yy = self.mem_h - yy - 1

        # Set the bit in the image buffer.
        addr = xx // 8 + yy * self.byte_w
        current = self.img[addr]
        if color == BLACK:
            self.img[addr] = current & ~(0x80 >> (xx % 8))
        else:
            self.img[addr] = current | (0x80 >> (xx % 8))

    def clear(self, color):
        for y in range(self.byte_h):
            for x in range(self.byte_w):
                addr = x + y * self.byte_w
                self.img[addr] = color

    def draw_point(self, x, y, color, dot_pixel, dot_style):
        if x >= self.w or y >= self.h:
            return
        if dot_style == AROUND:
            for xd in range(2 * dot_pixel - 1):
                for yd in range(2 * dot_pixel - 1):
                    self.set_pixel(x + xd - dot_pixel, y + yd - dot_pixel, color)
        else:
            for xd in range(dot_pixel):
                for yd in range(dot_pixel):
                    self.set_pixel(x + xd - 1, y + yd - 1, color)

    def draw_line(self, x1, y1, x2, y2, color, dot_pixel, line_type):
        x = x1
        y = y1
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        p = dx - dy
        xdir = -1 if x1 > x2 else 1
        ydir = -1 if y1 > y2 else 1
        dot_cnt = 0
        while True:
            dot_cnt += 1
            if line_type == LINE_DOTTED and dot_cnt % 3 == 0:
                self.draw_point(x, y, color, dot_pixel, AROUND)
            elif line_type == LINE_SOLID:
                self.draw_point(x, y, color, dot_pixel, AROUND)
            if x == x2 and y == y2:
                break
            e2 = 2 * p
            if e2 >= -dy:
                p -= dy
                x += xdir
            if e2 <= dx:
                p += dx
                y += ydir

    def draw_rectangle(self, x1, y1, x2, y2, color, fill, dot_pixel):
        if fill == FILL_FULL:
            for i in range(y1, y2):
                self.draw_line(x1, i, x2, i, color, dot_pixel, LINE_SOLID)
        elif fill == FILL_EMPTY:
            self.draw_line(x1, y1, x2, y1, color, dot_pixel, LINE_SOLID)
            self.draw_line(x1, y1, x1, y2, color, dot_pixel, LINE_SOLID)
            self.draw_line(x1, y2, x2, y2, color, dot_pixel, LINE_SOLID)
            self.draw_line(x2, y1, x2, y2, color, dot_pixel, LINE_SOLID)

    def draw_circle(self, x, y, r, color, fill, dot_pixel):
        dx = 0
        dy = r
        d = 1 - r
        while dy > dx:
            if fill == FILL_EMPTY:
                self.draw_point(x + dx, y + dy, color, dot_pixel, AROUND)
                self.draw_point(x + dy, y + dx, color, dot_pixel, AROUND)
                self.draw_point(x - dx, y + dy, color, dot_pixel, AROUND)
                self.draw_point(x - dy, y + dx, color, dot_pixel, AROUND)
                self.draw_point(x - dx, y - dy, color, dot_pixel, AROUND)
                self.draw_point(x - dy, y - dx, color, dot_pixel, AROUND)
                self.draw_point(x + dx, y - dy, color, dot_pixel, AROUND)
                self.draw_point(x + dy, y - dx, color, dot_pixel, AROUND)
            elif fill == FILL_FULL:
                for i in range(dx, dy):
                    self.draw_point(x + dx, y + i, color, dot_pixel, AROUND)
                    self.draw_point(x + i, y + dx, color, dot_pixel, AROUND)
                    self.draw_point(x - dx, y + i, color, dot_pixel, AROUND)
                    self.draw_point(x - i, y + dx, color, dot_pixel, AROUND)
                    self.draw_point(x - dx, y - i, color, dot_pixel, AROUND)
                    self.draw_point(x - i, y - dx, color, dot_pixel, AROUND)
                    self.draw_point(x + dx, y - i, color, dot_pixel, AROUND)
                    self.draw_point(x + i, y - dx, color, dot_pixel, AROUND)
            if d < 0:
                d += 2 * dx + 3
            else:
                d += 2 * (dx - dy) + 5
                dy -= 1
            dx += 1

    def draw_str(self, x, y, text_str, color, font_size, font):
        # Create a mask for the text.
        str_list = list(font.getmask(text=text_str, mode="1"))
        str_size = font.getsize(text=text_str)
        font_act_h = int(len(str_list) / (str_size[0]))
        font_h = font_size
        top_add_row = (font_h - font_act_h) // 2
        bot_add_row = (font_h - font_act_h) - top_add_row
        for i in range(top_add_row * str_size[0]):
            str_list.insert(0, 0)
        for i in range(bot_add_row * str_size[0]):
            str_list.append(0)
        # Invert the bits (if needed) so that 0 is black.
        str_list = [0 if b else 1 for b in str_list]
        n = 0
        for i in range(x, x + font_h):
            for j in range(y, y + str_size[0]):
                if str_list[n] == 0:
                    self.set_pixel(i, j, color)
                n += 1

#----------------------------
# Main Code: Load and display image
#----------------------------
def convert_image_to_epd_array(image_path, width, height):
    """
    Open an image, resize to (width, height), convert to 1-bit,
    and output a byte array (as a list) of length = (width//8+1)*height.
    """
    im = Image.open(image_path)
    im = im.resize((width, height))
    im = im.convert("1")  # Convert image to 1-bit mode.
    raw_bytes = im.tobytes()
    bytes_per_row = (width // 8) + 1  # driver expects extra byte padding
    expected_total = bytes_per_row * height
    # Pad with white (0xFF) if necessary:
    if len(raw_bytes) < expected_total:
        raw_bytes += bytes([0xFF] * (expected_total - len(raw_bytes)))
    elif len(raw_bytes) > expected_total:
        raw_bytes = raw_bytes[:expected_total]
    return list(raw_bytes)

if __name__ == '__main__':
    # File path for your image
    image_path = "/home/bruh/Desktop/QR code.bmp"

    # Convert the image to the required EPD byte array (expected 4000 bytes)
    gImage_custom = convert_image_to_epd_array(image_path, EPD_WIDTH, EPD_HEIGHT)
    print("gImage_custom length:", len(gImage_custom))
    
    # Create the GUI object.
    gui = EPD_GUI()

    # Initialize the display quickly
    gui.epd.hw_init_fast()

    # Write the image to the e-paper.
    gui.epd.whitescreen_all_fast(gImage_custom)
    time.sleep(2)  # Pause 2 seconds so you can see the image.

    # Put the e-paper display to deep sleep.
    gui.epd.sleep()

    # Clean up GPIO resources.
    gui.epd.clean_gpio()
