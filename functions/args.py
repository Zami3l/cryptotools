#!/usr/bin/python3
# coding : utf-8

import sys
from functions import hashing, hashing_custom, encoding, encryption, tools 
import getpass
from functions.color import red
from colored import stylize

def action(mode):

    # Input
    if mode.text is not None:
        
        data = mode.text.encode('utf8')
       
    elif mode.file is not None:

        data = tools.read(mode.file)
    
    elif mode.pwd:

        data = getpass.getpass("> ").encode('utf-8')

    # Encryption
    if mode.key is not None:
        key = mode.key.encode('utf-8')

    if mode.rot13:
        data = encryption.Shift_Cipher().ascii_letter(data, 13, 1)

    if mode.caesar:
        if mode.shift is None:
            missing('caesar', '--shift NUMBER')
        else:
            if mode.caesar == 'letter':
                data = encryption.Shift_Cipher().ascii_letter(data, mode.shift, mode.repeat)
            if mode.caesar == 'ascii':
                data = encryption.Shift_Cipher().ascii_extented(data, mode.shift, mode.repeat)
    
    if mode.vigenere:
        if mode.key is None:
            missing('key', '-k, --key KEY')
        else:
            if mode.vigenere == 'letter':
                data = encryption.Substitution_Cipher().ascii_letter(data, key)
            if mode.vigenere == 'ascii':
                data = encryption.Substitution_Cipher().ascii_extented(data, key)

    if mode.xor:
        if mode.key is None:
            missing('xor', '-k / --key KEY')
        else:
            data = encryption.Xor_Cipher().xor(data, key)

    if mode.rc4:
        if mode.key is None:
            missing('xor', '-k / --key KEY')
        else:
            data = encryption.RC4().cipher(data, key)

    # Hashing
    if mode.sha1:
        data = hashing.sha1(data)
    
    if mode.sha256:
        data = hashing.sha256(data)

    if mode.sha512:
        data = hashing.sha512(data)
    
    if mode.md5:
        data = hashing.md5(data)
    
    if mode.test:
        data = hashing_custom.Hash_Custom("functions/conf.toml").exec(data)
    
    # Encoding
    if mode.base16:
        data = encoding.b16(data)
    
    if mode.base32:
        data = encoding.b32(data)

    if mode.base64:
        data = encoding.b64(data)
    
    if mode.hex:
        data = encoding.hex(data)

    # View data
    if mode.view:
        # Uppercase data
        if mode.upper:
            print(data.decode('utf8').upper())
        else:
            print(data.decode('utf8'))

    # Copy data
    if mode.clip:
        clipboard.copy(data.decode('utf8'))

    # Output
    if mode.output is not None:
        tools.write(data, mode.output)

def missing(arg, argsRequired):

    sys.exit(stylize("The following arguments are required with {}: {}", red).format(arg, argsRequired))
