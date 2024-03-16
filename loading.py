import sys
import time

def loading_animation():
    animation = "|/-\\"
    for i in range(20):
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()
        time.sleep(0.1)

loading_animation()
print("\nLoading selesai.")