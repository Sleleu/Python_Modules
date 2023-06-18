from time import time, sleep
import sys

def ft_progress(lst) :
    start_time = time()
    count = len(lst)
    bar_length = 20
    for i in range(count) :
        elapsed_time = time() - start_time
        rate = (i + 1) / count
        eta = elapsed_time / rate - elapsed_time
        percentage = 100 if i == count - 1 else (i / count * 100)
        bar = '=' * int(((percentage / 100) * bar_length) - 1) + '>'
        sys.stdout.write(f"\rETA: {eta:.2f}s [{str(int(percentage)).rjust(3, ' ')}%]")
        sys.stdout.write(f" [{bar.ljust(bar_length,' ')}] ")
        sys.stdout.write(f" {i + 1}/{count} ")
        sys.stdout.write(f"| elapsed time {elapsed_time:.2f}s")
        sys.stdout.flush()
        yield i

listy = range(1000)
ret = 0
for elem in ft_progress(listy):
    ret += (elem + 3) % 5
    sleep(0.01)
print()
print(ret)