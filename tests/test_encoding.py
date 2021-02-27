#!/usr/bin/python3
# coding : utf-8

import unittest
from modules.encoding.base import b16, b32, b64, hex

class Test_Encoding(unittest.TestCase):

    plainText = "Zami3l".encode('utf8')

    def test_b16(self):

        self.assertEqual(b16('E' ,self.plainText), b'5A616D69336C')

    def test_b32(self):

        self.assertEqual(b32('E' ,self.plainText), b'LJQW22JTNQ======')

    def test_b64(self):

        self.assertEqual(b64('E' ,self.plainText), b'WmFtaTNs')

    def test_hex(self):

        self.assertEqual(hex('E' ,self.plainText), b'5a616d69336c')
