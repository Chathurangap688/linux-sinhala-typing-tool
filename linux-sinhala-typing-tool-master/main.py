import pyxhook
from array import array
import data_tree as data
import unicod as uni
import keyboard
import sys
import type
import os

reload(sys)
sys.setdefaultencoding('utf-8')
#change this to your log file's path
#this function is called everytime a key is pressed.

root = data.Tree('*')
root = uni.add_unicode(root)
capture_keys=True
i = 0
array = ""
def OnKeyPress(event):
  #if programe is enabled further text process will be done
  global capture_keys
  if capture_keys :
    global array
    global root
    global keyboard
    a = event.Ascii
    if ((a> 96)&(a< 123))|((a> 70)&(a< 91)):
      if(a!=85):
        array += event.Key
       
    
    #remove unwanted char for backspaces
    if(event.Key == "BackSpace"):
      array = array[:-1]
    if a == 32:
      #pause the key capturing
      capture_keys=False
      #print on terminal for development needs
      #print(uni.get_unicode(root,array[1:]))
      if(array == " "):
        return
      text = uni.get_unicode(root,array)
      lenth = len(array)
      array= ''

      
      #neglect if array is null
      if(text):
        #remove last space
        #keyboard.press_and_release('BackSpace')
        #remove english input

        
        text = text.lower()
        array = ""
        type.type_unicode(text,capture_keys,lenth)
        array = ""
        text = ""
        
      capture_keys=True

  if event.Ascii==96: #96 is the ascii value of the grave key (`)    
    new_hook.cancel()
#instantiate HookManager class
new_hook=pyxhook.HookManager()
#listen to all keystrokes
new_hook.KeyDown=OnKeyPress
#hook the keyboard
new_hook.HookKeyboard()
#start the session
new_hook.start()
