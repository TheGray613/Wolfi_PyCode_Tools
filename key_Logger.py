import pynput.keyboard
def windowsapi(key):
    print (key)
key_listener = pynput.keyboard.Listener(on_press=windowsapi)
with key_listener:
    key_listener.join()
