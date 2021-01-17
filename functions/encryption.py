#!/usr/bin/python3
# coding : utf-8


class Shift_Cipher:

    def ascii_letter(self, plainText, shift, repetition):

        for index in range(repetition):

            cipherText = []

            for ror in plainText:
                
                #Lowercase
                if ror.islower():
                    cipherText.append(chr((ord(ror)+(shift+index)-97)%26+97))

                #Uppercase
                elif ror.isupper():
                    cipherText.append(chr((ord(ror)+(shift+index)-65)%26+65))

                #If other, none shift
                else:
                    cipherText.append(ror)

        return ''.join(cipherText)


    def ascii_extented(self, plainText, shift, repetition):
        
        for index in range(repetition):

            cipherText = []

            for ror in plainText:

                cipherText.append(chr((ord(ror)+(shift+index))%256))

        return ''.join(cipherText)


class Xor_Cipher():

    def xor(self, plainText, key):
        
        cipherText = bytearray(plainText)

        for index in range(len(cipherText)):
            cipherText[index] ^= ord(key[index%len(key)])
        
        return cipherText
