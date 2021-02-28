#!/usr/bin/python3
# coding : utf-8

import unittest

from modules.encryption.rc4 import RC4
from modules.encryption.shift_cipher import Shift_Cipher
from modules.encryption.substitution_cipher import Substitution_Cipher
from modules.encryption.xor_cipher import Xor_Cipher

class Test_Encryption(unittest.TestCase):

    plainText = "Hi there, I'm Zami3l".encode('utf8')
    key = "Zami3l".encode('utf-8')

    def test_shift_cipher(self):
        
        cipherText = Shift_Cipher().ascii_letter('E', self.plainText, 8, 3)
        self.assertEqual(cipherText.decode('utf8'), "Rs drobo, S'w Jkws3v")
        plainText = Shift_Cipher().ascii_letter('D', cipherText, 8, 3)
        self.assertEqual(plainText, self.plainText)

        cipherText = Shift_Cipher().ascii_extented('E' ,self.plainText, 8, 3)
        self.assertEqual(cipherText.decode('utf8'), "Rs*~ro|o6*S1w*dkws=v")
        plainText = Shift_Cipher().ascii_extented('D', cipherText, 8, 3)
        self.assertEqual(plainText, self.plainText)

    def test_substitution_cipher(self):
        
        cipherText = Substitution_Cipher().ascii_letter('E', self.plainText, self.key)
        self.assertEqual(cipherText.decode('utf8'), "Gi fpecd, I'y Haxh3l")
        plainText = Substitution_Cipher().ascii_letter('D', cipherText, self.key)
        self.assertEqual(plainText, self.plainText)
