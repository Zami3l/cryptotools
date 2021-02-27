#!/usr/bin/python3
# coding : utf-8

import unittest

from modules.hashing.md import md5
from modules.hashing.sha import sha1, sha256, sha512
from modules.hashing.sha_custom import Sha_Custom

class Test_Hashing(unittest.TestCase):

    plainText = "Zami3l".encode('utf8')

    def test_sha1(self):
        
        self.assertEqual(sha1(self.plainText), b'2eadd9b2efee2fa9d57797212db07dd42179802e')

    def test_sha256(self):
        
        self.assertEqual(sha256(self.plainText), b'1df2903b3a35392ebe057c308eb5373d223f28888d305c03c86b4cc1461e507a')

    def test_sha512(self):
        
        self.assertEqual(sha512(self.plainText), b'd06dee8ce4949a8127a7dfeeaa250527ac49815df4935eeb488e5698b82225f61dddd4cf86d8f8c051c9eadc54a8d41c844f0bd890df3b22d37ea74eb6224c80')

    def test_md5(self):
        
        self.assertEqual(md5(self.plainText), b'99bb9aa6424951c098a43ae772732055')
