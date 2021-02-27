#!/usr/bin/python3
# coding : utf-8

import unittest
from modules.encoding.base import b16, b32, b64, hex

class Test_Encoding(unittest.TestCase):

    plainText = "Zami3l".encode('utf8')

    def test_b16(self):

        encodeText = b16('E' ,self.plainText)
        self.assertEqual(encodeText, b'5A616D69336C')
        decodeText = b16('D' , encodeText)
        self.assertEqual(decodeText, self.plainText)

    def test_b32(self):

        encodeText = b32('E' ,self.plainText)
        self.assertEqual(encodeText, b'LJQW22JTNQ======')
        decodeText = b32('D' ,encodeText)
        self.assertEqual(decodeText, self.plainText)

    def test_b64(self):

        encodeText = b64('E' ,self.plainText)
        self.assertEqual(encodeText, b'WmFtaTNs')
        decodeText = b64('D' ,encodeText)
        self.assertEqual(decodeText, self.plainText)

    def test_hex(self):

        encodeText = hex('E' ,self.plainText)
        self.assertEqual(encodeText, b'5a616d69336c')
        decodeText = hex('D' ,encodeText)
        self.assertEqual(decodeText, self.plainText)
