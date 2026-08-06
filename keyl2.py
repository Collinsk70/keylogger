from pynput import keyboard
import sys

def on_press (key):
    try:
        sys.stdout.write(key.char)
        sys.stdout.flush()

    except AttributeError:
        if key == keyboard.Key.enter:
            sys.stdout.write("\n")
        elif key == keyboard.Key.tab:
            sys.stdout.write("\t")
        elif key == keyboard.Key.space:
            sys.stdout.write(" ")
        elif
