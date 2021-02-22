#!/usr/bin/python3
# coding : utf-8

import logging

def read(file):

    with open(file, 'rb') as file:

        fileRead = file.read()
        logging.debug('\n===READ FILE===\n%s\n===============', fileRead)

        return fileRead

def write(data, file):

    with open(file, 'wb') as file:

        logging.debug('\n===WRITE FILE===\n%s\n================', data)
        file.write(data)

def letter_position(letter):
    
    # Lowercase
    if letter >= 97 and letter <= 122:
    
        return letter - 97
    
    # Uppercase
    elif letter >= 65 and letter <= 90:

        return letter - 65
    
    else:

        return 0

def case_letter(letter):
    
    # Lowercase
    if letter >= 97 and letter <= 122:
    
        return 'lowercase'
    
    # Uppercase
    elif letter >= 65 and letter <= 90:

        return 'uppercase'

    # Other
    else:

        return 'other'
