#!/usr/bin/python3
# coding : utf-8

import unittest
from functions import encryption

class Test_Encryption(unittest.TestCase):

    plainText = "Hi there, I'm Zami3l".encode('utf8')
    key = "Zami3l".encode('utf-8')

    def test_shift_cipher(self):
        
        cipherText = encryption.Shift_Cipher().ascii_letter(self.plainText, 8, 3).decode('utf8')
        self.assertEqual(cipherText, "Rs drobo, S'w Jkws3v")

        cipherText = encryption.Shift_Cipher().ascii_extented(self.plainText, 8, 3).decode('utf8')
        self.assertEqual(cipherText, "Rs*~ro|o6*S1w*dkws=v")

    def test_substitution_cipher(self):
        
        cipherText = encryption.Substitution_Cipher().ascii_letter(self.plainText, self.key).decode('utf8')
        self.assertEqual(cipherText, "Gi fpecd, I'y Haxh3l")
