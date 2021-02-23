#!/usr/bin/python3
# coding : utf-8

import logging
from functions.tools import letter_position, case_letter

class Shift_Cipher:

    def ascii_letter(self, plainText, shift, repetition):

        for index in range(repetition):

            cipherText = []

            for ror in plainText.decode('utf-8'):
                
                #Lowercase
                if ror.islower():
                    cipherText.append(chr((ord(ror)+(shift+index)-97)%26+97))

                #Uppercase
                elif ror.isupper():
                    cipherText.append(chr((ord(ror)+(shift+index)-65)%26+65))

                #If other, none shift
                else:
                    cipherText.append(ror)

            logging.info('#%d : %s', index+1, ''.join(cipherText))

        return ''.join(cipherText).encode('utf-8')

    def ascii_extented(self, plainText, shift, repetition):
        
        for index in range(repetition):

            cipherText = []

            for ror in plainText.decode('utf-8'):

                cipherText.append(chr((ord(ror)+(shift+index))%256))

            logging.info('#%d : %s', index+1, ''.join(cipherText))

        return ''.join(cipherText).encode('utf-8')

class Xor_Cipher():

    def xor(self, plainText, key):
        
        cipherText = bytearray(plainText)

        for index in range(len(cipherText)):

            cipherText[index] ^= key[index%len(key)]
        
        return cipherText


class Substitution_Cipher():

    def ascii_letter(self, plainText, key):

        cipherText = bytearray(len(plainText))
        iShift, iKey = 0, 0 # Si le plainText contient un caractère spécial il faut revenir à l'index précédent

        for iLetter in plainText:

            shiftLetter = (letter_position(iLetter) + letter_position(key[(iKey - iShift) % len(key)])) % 26

            if case_letter(iLetter) == 'lowercase':

                cipherText.append(shiftLetter + 97)

            elif case_letter(iLetter) == 'uppercase':

                cipherText.append(shiftLetter + 65)

            else:

                cipherText.append(iLetter)
                iShift += 1

            iKey += 1

        return cipherText
