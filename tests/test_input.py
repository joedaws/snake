#!/usr/bin/env python3
"""
Prints the scan code of all currently pressed keys.
Updates on every keyboard event.
"""
import sys
sys.path.append('..')
import keyboard
import time


def main():
    global is_running
    is_running = True

    def stop_running():
        global is_running
        is_running = False

    def up_signal():
        print('\nup')

    def left_signal():
        print('\nleft')

    def down_signal():
        print('\ndown')

    def right_signal():
        print('\nright')

    anim = ['|', '\\', '-', '/']
    i = 0

    # set up hotkeys
    keyboard.add_hotkey('space', stop_running)
    keyboard.add_hotkey('w', up_signal)
    keyboard.add_hotkey('a', left_signal)
    keyboard.add_hotkey('s', down_signal)
    keyboard.add_hotkey('d', right_signal)

    while is_running:
        time.sleep(0.17)
        # print the current frame
        print('\r ' + anim[i % 4], end='')

        # stop if the is_running flag has been turned off
        if not is_running:
            print('\nspace was pressed')
            print('goodbye')

        if i < 1000:
            i += 1
        else:
            i = 0


def print_pressed_keys(e):
    for code in keyboard._pressed_events:
        print(code)

def main2():
    keyboard.hook(print_pressed_keys)
    keyboard.wait()

if __name__ == "__main__":
    main2()
