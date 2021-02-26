#!/usr/bin/python3
# coding : utf-8

import sys, unittest

from modules.encoding.base import b16, b32, b64, hex

from modules.encryption.rc4 import RC4
from modules.encryption.shift_cipher import Shift_Cipher
from modules.encryption.substitution_cipher import Substitution_Cipher
from modules.encryption.xor_cipher import Xor_Cipher

from modules.hashing.sha import sha1, sha256, sha512
from modules.hashing.md import md5
from modules.hashing.sha_custom import Sha_Custom

import getpass

from modules.libs.color import red
from colored import stylize

def args_action(mode):

    # Input
    if mode.input is not None:
        data = mode.input.encode('utf8')
       
    elif mode.file is not None:
        data = tools.read(mode.file)
    
    elif mode.pwd:
        data = getpass.getpass("> ").encode('utf-8')

    # Uppercase
    mode.type = mode.type.upper()

    # Encoding Input
    if mode.type == 'D':

        if mode.base16:
            data = b16(mode.type, data)
        
        if mode.base32:
            data = b32(mode.type, data)

        if mode.base64:
            data = b64(mode.type, data)
        
        if mode.hex:
            data = hex(mode.type, data)

    # Encryption
    if mode.key is not None:
        key = mode.key.encode('utf-8')

    if mode.rot13:
        data = Shift_Cipher().ascii_letter(data, 13, 1)

    if mode.caesar:
        if mode.shift is None:
            missing('caesar', '--shift NUMBER')
        else:
            if mode.caesar == 'letter':
                data = Shift_Cipher().ascii_letter(mode.type, data, mode.shift, mode.repeat)
            if mode.caesar == 'ascii':
                data = Shift_Cipher().ascii_extented(mode.type, data, mode.shift, mode.repeat)
    
    if mode.vigenere:
        if mode.key is None:
            missing('key', '-k, --key KEY')
        else:
            if mode.vigenere == 'letter':
                data = Substitution_Cipher().ascii_letter(mode.type, data, key)
            if mode.vigenere == 'ascii':
                data = Substitution_Cipher().ascii_extented(mode.type, data, key)

    if mode.xor:
        if mode.key is None:
            missing('xor', '-k / --key KEY')
        else:
            data = Xor_Cipher().xor(data, key)

    if mode.rc4:
        if mode.key is None:
            missing('xor', '-k / --key KEY')
        else:
            data = RC4().cipher(mode.type, data, key)

    # Hashing
    if mode.sha1:
        data = sha1(data)
    
    if mode.sha256:
        data = sha256(data)

    if mode.sha512:
        data = sha512(data)
    
    if mode.md5:
        data = md5(data)
    
    if mode.custom:
        data = Sha_Custom("functions/conf.toml").exec(data)
    
    # Encoding Output
    if mode.type == 'E':

        if mode.base16:
            data = b16(mode.type, data)
        
        if mode.base32:
            data = b32(mode.type, data)

        if mode.base64:
            data = b64(mode.type, data)
        
        if mode.hex:
            data = hex(mode.type, data)

    # View data
    if mode.view:
        # Uppercase data
        if mode.upper:
            print(data.decode('utf8', 'ignore').upper())
        else:
            print(data.decode('utf8', 'ignore'))

    # Copy data
    if mode.clip:
        clipboard.copy(data.decode('utf8', 'ignore'))

    # Output
    if mode.output is not None:
        tools.write(data, mode.output)

    if mode.test:
        suite = unittest.TestLoader().discover("tests")
        result = unittest.TextTestRunner(verbosity=2).run(suite)

def missing(arg, argsRequired):

    sys.exit(stylize("The following arguments are required with {}: {}", red).format(arg, argsRequired))
