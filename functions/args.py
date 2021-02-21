#!/usr/bin/python3
# coding : utf-8

import sys
from functions import hashing, hashing_custom, encoding, encryption, tools 

def action(mode):

    # Input
    if mode.text is not None:
        
        data = mode.text.encode('utf8')
       
    elif mode.file is not None:

        data = tools.read(mode.file)

    # Hashing
    if mode.sha1:
        result = hashing.sha1(data)
    
    if mode.sha256:
        result = hashing.sha256(data)

    if mode.sha512:
        result = hashing.sha512(data)
    
    if mode.md5:
        result = hashing.md5(data)
    
    if mode.test:
        result = hashing_custom.Hash_Custom("functions/conf.toml").exec(data)
    
    # Encoding
    if mode.base16:
        result = encoding.b16(data)
    
    if mode.base32:
        result = encoding.b32(data)

    if mode.base64:
        result = encoding.b64(data)
    
    # Encryption
    if mode.rot13:
        result = encryption.Shift_Cipher().ascii_letter(data, 13, 1)

    if mode.caesar:
        if mode.shift is None:
            missing('caesar', '--shift NUMBER')
        else:
            if mode.caesar == 'letter':
                result = encryption.Shift_Cipher().ascii_letter(data, mode.shift, mode.repeat)
            if mode.caesar == 'ascii':
                result = encryption.Shift_Cipher().ascii_extented(data, mode.shift, mode.repeat)
    
    if mode.xor:
        if mode.key is None:
            missing('xor', '-k / --key KEY')
        else:
            result = encryption.Xor_Cipher().xor(data, mode.key)

    # View result
    if mode.view:
        # Uppercase result
        if mode.upper:
            print(result.decode('utf8').upper())
        else:
            print(result.decode('utf8'))

    # Copy result
    if mode.clip:
        clipboard.copy(result.decode('utf8'))

    # Output
    if mode.output is not None:
        tools.write(result, mode.output)

def missing(arg, argsRequired):

    sys.exit("The following arguments are required with {}: {}".format(arg, argsRequired))
