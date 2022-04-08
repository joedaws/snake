#!/usr/bin/env python3

import time

nlines = 2
# scroll up to make room for output
print(f"\033[{nlines}S", end="")

# move cursor back up
print(f"\033[{nlines}A", end="")

# save current cursor position
print("\033[s", end="")

for t in range(10):
    # restore saved cursor position
    print("\033[u", end="")
    print(f"Line one @ {t}")
    print(f"Line two @ {t}")
    t += 1
    time.sleep(.5)
