#!/usr/bin/python3
# coding : utf-8

import logging
from modules.libs.letters import letter_case

class Shift_Cipher:

    def ascii_letter(self, mode, plainText, shift, repetition):

        for index in range(repetition):

            cipherText = bytearray()

            for ror in plainText:
                
                #Lowercase
                if letter_case(ror) == 'lowercase':
                    if mode == 'E':
                        cipherText.append((ror+(shift+index)-97)%26+97)
                    elif mode == 'D':
                        cipherText.append((ror-(shift+index)-97)%26+97)

                #Uppercase
                elif letter_case(ror) == 'uppercase':
                    if mode == 'E':
                        cipherText.append((ror+(shift+index)-65)%26+65)
                    elif mode == 'D':
                        cipherText.append((ror-(shift+index)-65)%26+65)

                #If other, none shift
                else:
                    cipherText.append(ror)

            logging.info('#%d : %s', index+1, cipherText.decode('utf8'))

        return cipherText

    def ascii_extented(self, mode, plainText, shift, repetition):
        
        for index in range(repetition):

            cipherText = bytearray()

            for ror in plainText:

                if mode == 'E':
                    cipherText.append((ror+(shift+index))%256)
                elif mode == 'D':
                    cipherText.append((ror-(shift+index))%256)


            logging.info('#%d : %s', index+1, cipherText.decode('utf8'))

        return cipherText
