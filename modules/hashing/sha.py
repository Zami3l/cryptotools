#!/usr/bin/python3
# coding : utf-8

import hashlib

def sha1(plainText):
    
    return hashlib.sha1(plainText).hexdigest().encode('utf8')

def sha256(plainText):
    
    return hashlib.sha256(plainText).hexdigest().encode('utf8')

def sha512(plainText):
    
    return hashlib.sha512(plainText).hexdigest().encode('utf8')
