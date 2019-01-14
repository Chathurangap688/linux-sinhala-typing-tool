from pynput.keyboard import Key, Controller

keyboard = Controller()

def typeUni(word,state,len):
    if(word == False):
        state = False
        return 
    word = word.replace('*','')
    if(state):
     
        len += 'd'
        for x in len:
            #print(word)
            keyboard.press(Key.backspace)
            keyboard.release(Key.backspace)
        #keyboard.press(Key.right)
        #keyboard.release(Key.right)
        #keyboard.type(' : ')
        word = word.replace("\\","")

        #print(word)
        for x in word:
            
            if((x == 'u')|(x == 'U')):
                with keyboard.pressed(Key.shift):
                     with keyboard.pressed(Key.ctrl):

                         keyboard.type('u')
            else:
                keyboard.type(x)


        # with keyboard.pressed(Key.shift):
        #     with keyboard.pressed(Key.ctrl):
        #         keyboard.type(word)
        keyboard.type(' ')
        keyboard.type(' ')
        
        state = False
    
    return state 
