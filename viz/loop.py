#!/usr/bin/env python3

import time

def wait():
    animation = "|/-\\"
    idx = 0
    engaged = True
    while engaged:
        print(animation[idx % len(animation)], end='\r')
        idx += 1
        time.sleep(0.1)
        if idx > 100:
            engaged = False


def sleep_for(duration: int):
    # this is sleep in seconds
    time.sleep(duration)

if __name__ == "__main__":
    wait()
