from pynput import keyboard
import os


def on_release(key):
    if key == keyboard.Key.esc:
        # Stop whole program
        os._exit(1)
        return False


def escape_on_escape():
    listener = keyboard.Listener(
        on_release=on_release)
    listener.start()


if __name__ == "__main__":
    escape_on_escape()
