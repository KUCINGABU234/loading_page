import tkinter as tk
from tkinter import ttk
import time

def run_progressbar():
    progress_bar.start(10)
    for _ in range(100):
        time.sleep(0.1)
        progress_bar.step(1)
        root.update()
    progress_bar.stop()

root = tk.Tk()
root.title("Loading Bar")

frame = ttk.Frame(root, padding="20")
frame.grid(row=0, column=0)

progress_bar = ttk.Progressbar(frame, orient="horizontal", length=300, mode="determinate")
progress_bar.grid(row=0, column=0, padx=5, pady=5)

start_button = ttk.Button(frame, text="Start", command=run_progressbar)
start_button.grid(row=1, column=0, pady=5)

root.mainloop()