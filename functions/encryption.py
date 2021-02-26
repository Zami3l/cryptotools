#!/usr/bin/python3
# coding : utf-8

import logging
from functions.tools import letter_position, case_letter

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

class Xor_Cipher():

    def xor(self, plainText, key):
        
        cipherText = bytearray(plainText)

        for index in range(len(cipherText)):

            cipherText[index] ^= key[index%len(key)]
        
        return cipherText


class Substitution_Cipher():

    def ascii_letter(self, mode, plainText, key):

        cipherText = bytearray()
        iShift, iKey = 0, 0 # Si le plainText contient un caractère spécial il faut revenir à l'index précédent

        for iLetter in plainText:

            if mode == 'E':
                shiftLetter = (letter_position(iLetter) + letter_position(key[(iKey - iShift) % len(key)])) % 26
            else:
                shiftLetter = (letter_position(iLetter) - letter_position(key[(iKey - iShift) % len(key)])) % 26


            if case_letter(iLetter) == 'lowercase':

                cipherText.append(shiftLetter + 97)

            elif case_letter(iLetter) == 'uppercase':

                cipherText.append(shiftLetter + 65)

            else:

                cipherText.append(iLetter)
                iShift += 1

            iKey += 1

        return cipherText

class RC4():

    nbIterations = 256

    #Key Scheduling Algorithm
    def KSA(self, key):

        #Init
        S = list(range(self.nbIterations))
        j = 0
        keySize = len(key)

        for i in range(self.nbIterations):

            j = (j + S[i] + key[i % keySize]) % self.nbIterations
            S[i], S[j] = S[j], S[i] #Swap i and j

        return S

    #Pseudo-random generation algorithm
    def PRGA(self, S):

        #Init
        i = 0
        j = 0

        while True:

            i = (i + 1) % self.nbIterations
            j = (j + S[i]) % self.nbIterations
            S[i], S[j] = S[j], S[i] #Swap i and j
            K = S[(S[i] + S[j]) % self.nbIterations]

            yield K

    def cipher(self, mode, plainText, key):

        keystream = self.PRGA(self.KSA(key))
        result = bytearray()

        for index in plainText:

            result.append(index ^ next(keystream))

        return result
