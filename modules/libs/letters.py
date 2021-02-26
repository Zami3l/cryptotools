#!/usr/bin/python3
# coding : utf-8

def letter_position(letter):
    
    # Lowercase
    if letter >= 97 and letter <= 122:
        return letter - 97
    
    # Uppercase
    elif letter >= 65 and letter <= 90:
        return letter - 65
    
    else:
        return 0

def letter_case(letter):
    
    # Lowercase
    if letter >= 97 and letter <= 122:
        return 'lowercase'
    
    # Uppercase
    elif letter >= 65 and letter <= 90:
        return 'uppercase'

    # Other
    else:
        return 'other'
