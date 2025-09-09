import board
import time

import adafruit_dotstar


import neopixel

pixel_pin = board.A2
num_pixels = 8

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.05, auto_write=False)

RED = (255, 0, 0)
ORANGE = (255, 128, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
WHITE = (255, 255, 255)
N = (0,0,0)

while True:
    pixels[0] = (RED)
    pixels.show()
    time.sleep(0.1)
    pixels[1] = (ORANGE)
    pixels.show()
    time.sleep(0.1)
    pixels[2] = (YELLOW)
    pixels.show()
    time.sleep(0.1)
    pixels[3] = (GREEN)
    pixels.show()
    time.sleep(0.1)
    pixels[4] = (CYAN)
    pixels.show()
    time.sleep(0.1)
    pixels[5] = (BLUE)
    pixels.show()
    time.sleep(0.1)
    pixels[6] = (PURPLE)
    pixels.show()
    time.sleep(0.1)
    pixels[7] = (WHITE)
    pixels.show()
    time.sleep(0.1)
    pixels[7] = (N)
    pixels.show()
    time.sleep(0.1)
    pixels[6] = (N)
    pixels.show()
    time.sleep(0.1)
    pixels[5] = (N)
    pixels.show()
    time.sleep(0.1)
    pixels[4] = (N)
    pixels.show()
    time.sleep(0.1)
    pixels[3] = (N)
    pixels.show()
    time.sleep(0.1)
    pixels[2] = (N)
    pixels.show()
    time.sleep(0.1)
    pixels[1] = (N)
    pixels.show()
    time.sleep(0.1)
    pixels[0] = (N)
    pixels.show()
    time.sleep(0.1)

led = adafruit_dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1)
led.brightness = 0.1


    

