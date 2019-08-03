from pyinput import keyboard
import pyperclip
import time
def get_key_name(key):
        if isinstance(key , keyboard.keycode):
                        return key.char
        else :
                        return str(key)

def on_press(key):
    print("key pressed {}".format(key))
    print("key type {}".format(key.__class__.__name__))

def on_release(key):
    print("{} key released " .format(key))
    if str(key) == "key.src":
        print("good")
        return False

with keyboard.Listner(on_press = on_press,on_release = on_release) as Listner:
    Listner.join()

list=[]

while = True:
    if pyperclip.paste () != 'None':
        value = pyperclip.paste()

        if value not in list:
            list.append(value)

        print(list)

        time.sleep(3)

