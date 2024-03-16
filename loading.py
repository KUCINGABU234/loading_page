from progressbar import ProgressBar
import time

# Membuat objek ProgressBar dengan gaya "Fancy"
pbar = ProgressBar(widgets=['Loading: ', ' ', progressbar.widgets.Bar(marker='■', left='[', right=']'), ' ', progressbar.widgets.Percentage(), ' ', progressbar.widgets.Timer()], maxval=10).start()

# Membuat range 
for i in range(10):
    time.sleep(0.5)  # Menggunakan sleep untuk simulasi pekerjaan yang sedang berlangsung
    pbar.update(i+1)

pbar.finish()