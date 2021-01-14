#!/usr/bin/python3
# coding : utf-8

import base64

def b16(plainText):
    
    return base64.b16encode(plainText.encode()).decode()

def b32(plainText):
    
    return base64.b32encode(plainText.encode()).decode()

def b64(plainText):
    
    return base64.b64encode(plainText.encode()).decode()
