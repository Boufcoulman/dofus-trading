from pynput import keyboard
import os


def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))


def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop whole program
        os._exit(1)
        return False


def escape_on_escape():
    listener = keyboard.Listener(
        on_press=on_press,
        on_release=on_release)
    listener.start()