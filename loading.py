import time
import os
import sys

def loading_animation():
    animation = "|/-\\"
    for i in range(20):
        sys.stdout.write("\rMemproses " + animation[i % len(animation)])
        sys.stdout.flush()
        time.sleep(0.4)

def clear_screen():
    # Membersihkan layar terminal atau command prompt
    os.system('cls' if os.name == 'nt' else 'clear')

# Memulai animasi loading
loading_animation()

# Membersihkan layar
clear_screen()

# Mendapatkan waktu saat ini
current_time = time.strftime("%H:%M:%S")

# Menampilkan waktu saat ini
print("JAM:", current_time)