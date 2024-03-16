import curses
import time

def loading_animation(window):
    window.clear()
    curses.curs_set(0)  # Hide the cursor
    window.addstr(0, 0, "Loading...")

    for i in range(1, 11):
        window.addstr(2, 0, "[" + "#" * i + "-" * (10 - i) + "]")
        window.refresh()
        time.sleep(8.5)

    window.addstr(4, 0, "Loading complete!")
    window.refresh()
    time.sleep(1)

def main(stdscr):
    loading_animation(stdscr)
    stdscr.getch()

curses.wrapper(main)