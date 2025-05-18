import curses
import time

def main(stdscr, num_bunnies):
    curses.curs_set(0)
    stdscr.nodelay(True)
    stdscr.timeout(100)

    start_bunny = [
        r" (\_/)",
        r" ( •_•)",
        r"/ >🍪<"
    ]

    mirrored_bunny = [
        r"(\_/ )",
        r"(•_• )",
        r"🍪< \\"
    ]

    height, width = stdscr.getmaxyx()
    x = 0
    direction = 1

    while True:
        stdscr.clear()

        bunny = start_bunny if direction == 1 else mirrored_bunny

        for idx in range(num_bunnies):
            y = 5 + idx * (len(bunny) + 1)
            for i, line in enumerate(bunny):
                if 0 <= y + i < height and 0 <= x < width:
                    stdscr.addstr(y + i, x, line)

        stdscr.refresh()
        time.sleep(0.05)

        x += direction
        max_bunny_width = max(len(line) for line in bunny)
        if x + max_bunny_width >= width or x <= 0:
            direction *= -1

        key = stdscr.getch()
        if key == ord('q'):
            break

if __name__ == "__main__":
    while True:
        try:
            num = int(input("How many bunnies do you want (1-10)? "))
            if 1 <= num <= 10:
                break
            else:
                print("Please enter a number between 1 and 10.")
        except ValueError:
            print("That's not a valid number. Try again.")

    curses.wrapper(main, num)

