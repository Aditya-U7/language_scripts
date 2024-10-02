import sys
import unicodedata


def print_characters(script_characters):

    print('\nCharacter | Code Point | Name \n')

    for character in script_characters:

        try:

            print(chr(character).center(10), end=' ')

            print(f'U+{character:04X}'.center(16), end=' ')

            print(unicodedata.name(chr(character), '<Reserved>'), end='\n\n')

            # print(unicodedata.category(chr(character)), end='\n\n') For category of the character.

        except ValueError:

            print('\n')

            continue
            
            
def take_user_choice(scripts):

    print('\nPlease select from the following scripts:\n')

    for choice in scripts:

        print(choice, end=' | ')

    print('\n')

    iteration_value = 3

    while True:

        user_input = input().strip().title()
        
        user_choice = ""
        
        count = 0
        
        length = len(user_input.split(' '))

        for word in user_input.split(' '):
            
            if word == 'And':
                
                user_choice += 'and'
            
            else:
                
                if word == 'Cjk':
                    user_choice += word.upper()    
                else:
                    user_choice += word
            
                    
            count +=1      
            
            if count != length:   
                user_choice += ' '    
               
        
        print('\n\n', user_choice, sep='')
        
        if user_choice not in scripts:

            print('\nOops! Invalid input.')

            iteration_value -= 1

            if iteration_value < 1:

                print('Program terminated.')
                sys.exit()

            print(
                '\nYOU WILL BE ASKED ',
                iteration_value,
                ' MORE TIMES BEFORE THE PROGRAM TERMINATES.',
            )

            print('\nPlease re-enter the script name from the above options:\n')

        else:

            return user_choice            


def generate_the_script():

    script_range = {
    
        'Alphabetic Presentation Forms': (0xFB1D, 0xFB4F),     
    
        'Arabic' : (0x0600, 0x06FF),
        
        'Basic Latin' : (0x0000, 0x007F),
        
        'CJK Unified Ideographs' : (0x4E00, 0x9FFF),
        
        'Egyptian Hieroglyphs' : (0x13000, 0x1342F),
        
        'Greek and Coptic' : (0x0370, 0x03FF),
        
        'Hebrew': (0x0590, 0x05FF),
        
        'Hirangana' : (0x3040, 0x309F),
        
        'Katana' : (0x30A0, 0x30FF)
        
    }
    
    user_choice = take_user_choice(script_range)

    start = script_range[user_choice][0]

    end = script_range[user_choice][1] + 1

    print('\n\nRange: ', end='')

    print(f'{start:04X}', '-', f'{(end - 1):04X}')
    
    return [i for i in range(start, end)]            
    
    
print('\nThis is a program for generating the characters of the various scripts.\n')

script_characters = generate_the_script()

print_characters(script_characters)    
