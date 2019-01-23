from pynput.keyboard import Key, Controller

keyboard = Controller()



def typeUni(word,state,len):            #arguments -  word - converted unicode values
                                        #             state -  true or false
                                        #             len -  user input word
    if(word == False):                 
        state = False
        return 
    
    word = word.replace('*','')

    if(state):
     
        len += 'd'
        for x in len:
            keyboard.press(Key.backspace)                  #erase the word, where user typed word by using backspace 
            keyboard.release(Key.backspace)                #each presses there should be button release.
        

                                                           #the unicode value is converted to sinhala letters
                                                           #with pressing shift + ctrl + unicode value
                                                           #this process is done here
        with keyboard.pressed(Key.shift):
            with keyboard.pressed(Key.ctrl):
                keyboard.type(word)
        keyboard.type(' ')                                 #after each word there should print a space
        
        state = False                                      #make status false
    
    return state                                           #return status