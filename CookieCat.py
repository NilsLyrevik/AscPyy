#hello this is a comment to start
import time
import os

frames = [
    r"""
     (\_/)
     ( •_•)
     / >🍪
    """,
    r"""
     (\_/)
     ( •_•)
     / 🍪<
    """,
    r"""
     (\_/)
     ( •_•)
     🍪< \
    """
]
while True:
    for frame in frames:
        os.system('cls' if os.name == 'nt' else 'clear') ## cls for Windows nt for Unix
        print(frame)
        time.sleep(0.5)
