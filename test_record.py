from pynput import keyboard
import os
import time


def on_press(key):
    print('key {0} pressed'.format(key))


def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop whole program
        os._exit(1)
        return False


def recoooord():
    listener = keyboard.Listener(
        on_press=on_press,
        on_release=on_release)
    listener.start()


if __name__ == "__main__":
    recoooord()
    time.sleep(100)
