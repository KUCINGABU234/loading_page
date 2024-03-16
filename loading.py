from tqdm import tqdm
import time

for i in tqdm(range(10), desc="Loading", bar_format="{l_bar}{bar} {n_fmt}/{total_fmt} [{elapsed}<{remaining}, {rate_fmt}{postfix}]"):
    time.sleep(0.5) 