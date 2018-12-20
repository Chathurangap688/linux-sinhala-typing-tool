
import pyxhook
from array import array
import data_tree as data
import unicod as uni
#change this to your log file's path

#this function is called everytime a key is pressed.

root = data.Tree('*')
root = uni.add_unicode(root)

i = 0
array = ""
def OnKeyPress(event):
  global array
  global root
  a = event.Ascii
  
  if ((a> 96)&(a< 123))|((a> 64)&(a< 91)):
      array += event.Key 
    #print(event.Key)
  if(event.Key == "BackSpace"):
    array = array[:-1]
  if a == 32:
      uni.get_unicode(root,array)
      array = ""

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
