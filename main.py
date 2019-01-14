from pynput import keyboard
import time
import type
import unicod
import data_tree as data

root = data.Tree('*')
root = unicod.add_unicode(root)

state = False
word = ""
def on_press(key):
    global root
    global state
    global word
    if(state):
        return
    if (key == keyboard.Key.esc):
        # Stop listener
        return False
    if (key == keyboard.Key.backspace):
        word = word[:-1]
    if(key ==  keyboard.Key.space):
        state = True
        temp_word = word
        word = ""
        uni_code = unicod.get_unicode(root,temp_word)
        #print(uni_code)
        state = type.typeUni(uni_code,state,temp_word)
        state =False
        word = ""
        

    try:
        #print(format(key.char))
        if(state):
            pass
        a=ord(key.char)
        #print(a)
        #print(word)
        if(a>124 | a<65):
            word = word[:-1]
            #print('wrong code')
            return
        print(format(key.char))
        word += format(key.char)
    except AttributeError:
        pass
        #print(format(key))


# Collect events until released
with keyboard.Listener(
        on_press=on_press) as listener:
    listener.join()
