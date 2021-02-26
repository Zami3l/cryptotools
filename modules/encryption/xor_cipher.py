#!/usr/bin/python3
# coding : utf-8

import logging

class Xor_Cipher():

    def xor(self, plainText, key):
        
        cipherText = bytearray(plainText)

        for index in range(len(cipherText)):

            cipherText[index] ^= key[index%len(key)]
        
        return cipherText
