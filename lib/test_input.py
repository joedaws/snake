#!/usr/bin/env python3
"""
Prints the scan code of all currently pressed keys.
Updates on every keyboard event.

SPACE has code 57
"""
import sys, select
sys.path.append('..')
import keyboard


def print_pressed_keys(e):
    line = ', '.join(str(code) for code in keyboard._pressed_events)
    # '\r' and end='' overwrites the previous line.
    # ' '*40 prints 40 spaces at the end to ensure the previous line is cleared.
    print('\r' + line + ' '*40, end='')

    if 57 in keyboard._pressed_events:
        print("\n I'm going to quit")


def on_triggered():
    print("Triggered!")


def wait_for_esc():
    print('Press and release your desired shortcut: ')
    shortcut = keyboard.read_hotkey()
    print('Shortcut selected:', shortcut)

    keyboard.add_hotkey(shortcut, on_triggered)

    print("Press ESC to stop.")
    keyboard.wait('esc')


def main():
    keyboard.hook(print_pressed_keys)
    keyboard.wait()


if __name__ == "__main__":
    # wait_for_esc()
    step = 0
    timeout = 2
    while True:
        print(step)

        i, o, char = select.select([sys.stdin], [], [], timeout)

        if i:
            print(i, o, char)

        # want to return control to this process
        # as soon as a button is pressed

        step += 1

        if step > 10:
            break
