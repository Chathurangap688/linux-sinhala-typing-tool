from pynput import keyboard
import time
import type
import unicod
import data_tree as data

root = data.Tree('*')                   #initializing tree for data_tree
root = unicod.add_unicode(root)
    
state = False   
word = ""                               #initializing word for store user input charactes
def on_press(key):
    global root
    global state
    global word
    if(state):                              #if state == true, stop the process
        return
    if (key == keyboard.Key.esc):           #if user presses esc button, stop the process
        # Stop listener
        return False
    if (key == keyboard.Key.backspace):     #if user presses backspace remove the last character from word
        word = word[:-1]
    if(key ==  keyboard.Key.space):         #if user presses space, the existing word valriable take as whole user input
        state = True
        temp_word = word
        word = ""                                           #make the wprd variable free
        uni_code = unicod.get_unicode(root,temp_word)       #pass the word to convert into sinhala unicode
        
        state = type.typeUni(uni_code,state,temp_word)      #pass the converted word to print
        state =False                                        #make status as false
                                                 
        

    try:
        
        if(state):
            pass
        a=ord(key.char)
        #print(a)
        #print(word)
        if(a>124 | a<65):
            word = word[:-1]
            #print('wrong code')
            return
        #print(format(key.char))
        word += format(key.char)
    except AttributeError:
        pass
        #print(format(key))


# Collect events until released
def panhidha():
    with keyboard.Listener(
            on_press=on_press) as listener:
        listener.join()
    #pyinstaller --onefile  