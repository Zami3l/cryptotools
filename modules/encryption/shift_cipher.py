#!/usr/bin/python3
# coding : utf-8

import logging

class Shift_Cipher:

    def ascii_letter(self, mode, plainText, shift, repetition):

        for index in range(repetition):

            cipherText = []

            for ror in plainText.decode('utf-8'):
                
                #Lowercase
                if ror.islower():
                    if mode == 'E':
                        cipherText.append(chr((ord(ror)+(shift+index)-97)%26+97))
                    elif mode == 'D':
                        cipherText.append(chr((ord(ror)-(shift+index)-97)%26+97))

                #Uppercase
                elif ror.isupper():
                    if mode == 'E':
                        cipherText.append(chr((ord(ror)+(shift+index)-65)%26+65))
                    elif mode == 'D':
                        cipherText.append(chr((ord(ror)-(shift+index)-65)%26+65))


                #If other, none shift
                else:
                    cipherText.append(ror)

            logging.info('#%d : %s', index+1, ''.join(cipherText))

        return ''.join(cipherText).encode('utf-8')

    def ascii_extented(self, mode, plainText, shift, repetition):
        
        for index in range(repetition):

            cipherText = []

            for ror in plainText.decode('utf-8'):

                if mode == 'E':
                    cipherText.append(chr((ord(ror)+(shift+index))%256))
                elif mode == 'D':
                    cipherText.append(chr((ord(ror)-(shift+index))%256))


            logging.info('#%d : %s', index+1, ''.join(cipherText))

        return ''.join(cipherText).encode('utf-8')
