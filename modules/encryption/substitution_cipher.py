#!/usr/bin/python3
# coding : utf-8

import logging
from modules.libs.letters import letter_position, letter_case

class Substitution_Cipher():

    def ascii_letter(self, mode, plainText, key):

        cipherText = bytearray()
        iShift, iKey = 0, 0 # Si le plainText contient un caractère spécial il faut revenir à l'index précédent

        for iLetter in plainText:

            if mode == 'E':
                shiftLetter = (letter_position(iLetter) + letter_position(key[(iKey - iShift) % len(key)])) % 26
            else:
                shiftLetter = (letter_position(iLetter) - letter_position(key[(iKey - iShift) % len(key)])) % 26


            if letter_case(iLetter) == 'lowercase':

                cipherText.append(shiftLetter + 97)

            elif letter_case(iLetter) == 'uppercase':

                cipherText.append(shiftLetter + 65)

            else:

                cipherText.append(iLetter)
                iShift += 1

            iKey += 1

        return cipherText
