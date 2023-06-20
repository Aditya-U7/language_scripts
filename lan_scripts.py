'''
Author: Aditya Upadhye

This program prints the Unicode characters of various Indian languages and also displays the information such as its code point and name.
'''

import unicodedata

def print_characters(unicode_characters):
    
    print("\nCharacter | Unicode Point | Name \n")

    for character in unicode_characters:
    
        try:
      
            print(chr(character).center(10), end=" ")
    
            print(f'U+{character:04x}'.center(16), end=" ")
    
            print(unicodedata.name(chr(character), "<Reserved>"), end="\n\n")
            
            #print(unicodedata.category(chr(emoji)), end="\n\n")  For category of the character.

        except ValueError:
             
            print("\n")
        
            continue
            

#unicode_characters = [i for i in range(int(0x0980), int(0x0a00))]      # Bengali script

#unicode_characters = [i for i in range(int(0x11000), int(0x11080))]   # Brahmi script

#unicode_characters = [i for i in range(int(0x0900), int(0x0980))]     # Devnagari script

#unicode_characters = [i for i in range(int(0x0a80), int(0x0b00))]     # Gujarati script

#unicode_characters = [i for i in range(int(0x0d00), int(0x0d80))]     # Malayalam script

unicode_characters = [i for i in range(int(0x0b80), int(0x0c00))]     # Tamil script

#unicode_characters = [i for i in range(int(0x0c00), int(0x0c80))]     # Telugu script 

print_characters(unicode_characters)
