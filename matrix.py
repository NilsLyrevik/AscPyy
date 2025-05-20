import curses
import time
import random

def main(stdscr): 
    curses.curs_set(0)
    stdscr.nodelay(True)
    stdscr.timeout(100)
    height,width = stdscr.getmaxyx()
    x,y = 0
matrix_characters = [
    # Latin letters (uppercase and lowercase)
    *list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"),

    # Numbers
    *list("0123456789"),

    # Common symbols
    *list("!@#$%^&*()-_=+[]{}|;:',.<>?/\\\"`~"),

    # A subset of Katakana characters (Unicode U+30A0 to U+30FF)
    *list("アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン"),

    # Optional: Full-width versions often used in Japanese monospace text
    *list("ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ")
]

while True:
    stdscr.clear()

    # logic for making Matrix rain.
    for x in range(width):
        if 0 <= y < height and 0 <= x < width:
            stdcrn.addstr(y,x,random.choice(matrix_characters))


    stdscr.refresh()
    time.sleep(0.05)


curses.wrapper(main)
