'''

Author: Aditya Upadhye

This program prints the Unicode characters of various language scripts and also displays the information such as its code point and name.

'''

import sys
import unicodedata

def print_characters(script_characters):
    
    print("\nCharacter | Unicode Point | Name \n")

    for character in script_characters:
    
        try:
      
            print(chr(character).center(10), end=" ")
    
            print(f'U+{character:04X}'.center(16), end=" ")
    
            print(unicodedata.name(chr(character), "<Reserved>"), end="\n\n")
            
            #print(unicodedata.category(chr(emoji)), end="\n\n")  For category of the character.

        except ValueError:
             
            print("\n")
        
            continue


def take_user_choice(scripts):

    print("\nPlease select from the following scripts:\n")
    
    for choice in scripts:
        
        print(choice, end=" ")
    
    print("\n")
    
    iteration_value = 3
    
    while (True):
    
        user_choice = input().capitalize()
        
        if user_choice not in scripts:
        
            print("\nOops! Invalid input.")
            
            iteration_value -= 1
            
            if iteration_value < 1:
                
                print("Program terminated.")
                sys.exit() 
                   
            print("\nYOU WILL BE ASKED ", iteration_value," MORE TIMES BEFORE THE PROGRAM TERMINATES.")  
                   
            print("\nPlease re-enter the script name from the above options:\n")
                
        
        else:
        
            return user_choice 
              
            
        
def generate_the_script(user_choice, scripts):

    script_range = {
         
         "Bengali": (0x0980, 0x0a00), "Brahmi" : (0x11000, 0x11080), "Devnagari" : (0x0900,0x0980), "Gujarati" : (0x0a80, 0x0b00), "Kannada" : (0x0c80, 0x0d00), 
         "Malayalam" : (0x0d00, 0x0d80), "Odia" : (0x0b00, 0x0b80), "Tamil" : (0x0b80, 0x0c00), "Telugu" : (0x0c00, 0x0c80)
         
         }
         
    
    start = script_range[user_choice][0]

    end = script_range[user_choice][1]

    return ([i for i in range(start, end)])


#################################         

scripts = ["Bengali", "Brahmi", "Devnagari", "Gujarati", "Kannada", "Malayalam", "Odia", "Tamil", "Telugu"]
       
print("\nHello, this is a program for printing the characters of various scripts along with their Unicode code points and names.\n")

user_choice = take_user_choice(scripts)    
             
script_characters = generate_the_script(user_choice, scripts)        

print_characters(script_characters)        
            

#script_characters = [i for i in range(int(0x0980), int(0x0a00))]     # Bengali script

#script_characters = [i for i in range(int(0x11000), int(0x11080))]   # Brahmi script

#script_characters = [i for i in range(int(0x0900), int(0x0980))]     # Devnagari script

#script_characters = [i for i in range(int(0x0a80), int(0x0b00))]     # Gujarati script

#script_characters = [i for i in range(int(0x0c80), int(0x0d00))]     # Kannada script

#script_characters = [i for i in range(int(0x0d00), int(0x0d80))]     # Malayalam script

#script_characters = [i for i in range(int(0x0b00), int(0x0b80))]     # Odia script        

#script_characters = [i for i in range(int(0x0b80), int(0x0c00))]     # Tamil script

#script_characters = [i for i in range(int(0x0c00), int(0x0c80))]     # Telugu script 


