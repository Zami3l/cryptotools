#!/usr/bin/python3
# coding : utf-8

import unittest
from functions import encoding

class Test_Encoding(unittest.TestCase):

    plainText = "Zami3l".encode('utf8')

    def test_b16(self):

        self.assertEqual(encoding.b16(self.plainText), b'5A616D69336C')

    def test_b32(self):

        self.assertEqual(encoding.b32(self.plainText), b'LJQW22JTNQ======')

    def test_b64(self):

        self.assertEqual(encoding.b64(self.plainText), b'WmFtaTNs')

    def test_hex(self):

        self.assertEqual(encoding.hex(self.plainText), b'5a616d69336c')
