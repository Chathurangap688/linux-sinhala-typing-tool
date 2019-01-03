import pyautogui

def type_unicode(word,state,lenth):
    #print(state)
    if(state):
        print(state)
        return
    for x in range(lenth+1):
        pyautogui.press('backspace')

    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('shift')
    pyautogui.typewrite(word)
    pyautogui.keyUp('ctrl')
    pyautogui.keyUp('shift')  
    pyautogui.press('space')

