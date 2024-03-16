import curses
import time

def loading_animation(window):
    window.clear()
    curses.curs_set(0)  # Hide the cursor
    window.addstr(0, 0, "Loading... (wait)")

    for i in range(1, 11):
        window.addstr(2, 0, "[" + "•" * i + "-" * (10 - i) + "]")
        window.refresh()
        time.sleep(0.5)

 import time
import os

def clear_screen():
    # Membersihkan layar terminal atau command prompt
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    # Membersihkan layar
    clear_screen()

    # Mendapatkan waktu saat ini
    current_time = time.strftime("%H:%M:%S")

    # Menampilkan waktu saat ini
    print("Jam Sekarang:", current_time)

    # Menunda pembaruan untuk setiap detik
    time.sleep(1)   window.addstr(4, 0, "Loading complete!")
    
    window.refresh()
    time.sleep(1)

def main(stdscr):
    loading_animation(stdscr)
    stdscr.getch()

curses.wrapper(main)