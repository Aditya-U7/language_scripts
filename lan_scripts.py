"""

Author: Aditya Upadhye

This program prints the Unicode characters of various language scripts along with their Unicode points and their character names. 

"""

import sys
import unicodedata


def print_characters(script_characters):

    print('\nCharacter | Unicode Point | Name \n')

    for character in script_characters:

        try:

            print(chr(character).center(10), end=' ')

            print(f'U+{character:04X}'.center(16), end=' ')

            print(unicodedata.name(chr(character), '<Reserved>'), end='\n\n')

            # print(unicodedata.category(chr(emoji)), end='\n\n')  For category of the character.

        except ValueError:

            print('\n')

            continue


def take_user_choice(scripts):

    print('\nPlease select from the following scripts:\n')

    for choice in scripts:

        print(choice, end=' ')

    print('\n')

    iteration_value = 3

    while True:

        user_choice = input().capitalize()

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


def generate_the_script(user_choice, scripts):

    script_range = {
        
        'Bengali': (0x0980, 0x09FF),
        
        'Brahmi': (0x11000, 0x1107F),
        
        'Devanagari': (0x0900, 0x097F),
        
        'Gujarati': (0x0A80, 0x0AFF),
        
        'Kannada': (0x0C80, 0x0CFF),
        
        'Malayalam': (0x0D00, 0x0D7F),
        
        'Odia': (0x0B00, 0x0B7F),
        
        'Tamil': (0x0B80, 0x0BFF),
        
        'Telugu': (0x0C00, 0x0C7F),
    }

    start = script_range[user_choice][0]

    end = script_range[user_choice][1] + 1

    print('\n\nRange: ', end='')

    print(f'{start:04X}', '-', f'{(end - 1):04X}')

    return [i for i in range(start, end)]


#################################

scripts = [
    
    'Bengali',
    'Brahmi',
    'Devanagari',
    'Gujarati',
    'Kannada',
    'Malayalam',
    'Odia',
    'Tamil',
    'Telugu',
]

print('\nThis is a program for generating the characters of the various scripts.\n')

user_choice = take_user_choice(scripts)

script_characters = generate_the_script(user_choice, scripts)

print_characters(script_characters)

