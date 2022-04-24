#!/usr/bin/env python3
from threading import Thread, Timer
import time




def main():
    """Get input of user from another thread."""
    timeout = 10
    t = Timer(timeout, print, ['Sorry, times up'])
    t.start()
    prompt = f"You have {timeout} seconds to choose the correct answer...\n"
    answer = input(prompt)
    t.cancel()


if __name__ == "__main__":
    main()
