#!/usr/bin/python3
# coding : utf-8

import hashlib

def md5(plainText):
    
    return hashlib.md5(plainText).hexdigest().encode('utf8')
