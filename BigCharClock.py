#large font time in cmd
import time
import os

import GlyphManager.GlyphManager as GlyphManager

def timer(chars):
    while True:
        os.system("cls")
        GlyphManager.BlockPrint(time.strftime("%H:%M:%S"),chars)
        time.sleep(0.75)

def padded_timer(chars):
    width, length = GlyphManager._get_terminal_size_windows()

    if width > 64 and length > 10: # 64 is char_width * 8 which represnts the number of characters in the timer, 11 is height of each char
        width_diff = width - 64
        length_diff = length - 10

        padx = width_diff / 2 / 8 # /2 to allow for the 2 sides to be even, and /8 as 1 char will fill 8 pixels
        pady = length_diff / 2 #we wont use the block print, as using indiv lines can be much more precise

    while True:
        os.system("cls")
        for _ in range(pady):
            print ""
        
        GlyphManager.BlockPrint(" " * padx + time.strftime("%H:%M:%S"),chars)
        time.sleep(0.9)


char_set = GlyphManager.loadChars()
padded_timer(char_set)
timer(char_set)

