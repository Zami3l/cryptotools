#!/usr/bin/python3
# coding : utf-8

import base64

def b16(mode, plainText):

    if mode == 'E':
        return base64.b16encode(plainText)

    elif mode == 'D':
        return base64.b16decode(plainText)
    

def b32(mode, plainText):
    
    if mode == 'E':
        return base64.b32encode(plainText)

    elif mode == 'D':
        return base64.b32decode(plainText)

def b64(mode, plainText):

    if mode == 'E':
        return base64.b64encode(plainText)

    elif mode == 'D':
        return base64.b64decode(plainText)

def hex(mode, plainText):

    if mode == 'E':
        return plainText.hex().encode('utf8')

    elif mode == 'D':
        return bytes.fromhex(plainText.decode('utf8'))
