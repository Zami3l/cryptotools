#!/usr/bin/python3
# coding : utf-8

import argparse, logging, sys
import clipboard
from functions import hashing, encoding, encryption, tools

def check_args(_agrs=None):
    
    # Init Argparse
    parser = argparse.ArgumentParser(description='Cryptotools')

    typeGroup = parser.add_mutually_exclusive_group()
    typeGroup.add_argument('--text', metavar='TEXT', help="Text for Encode/Hash/Encrypt")
    typeGroup.add_argument('--file', metavar='FILE', help="File for Encode/Hash/Encrypt")
    parser.add_argument('--output', metavar='OUTPUT', help="File output")

    encoding = parser.add_argument_group(title='Encoding')
    encoding.add_argument('--b16', action="store_true", help="Encode with base 16")
    encoding.add_argument('--b32', action="store_true", help="Encode with base 32")
    encoding.add_argument('--b64', action="store_true", help="Encode with base 64")

    hashing = parser.add_argument_group(title='Hashing')
    hashing.add_argument('--sha1', action="store_true", help="Use sha1 hash algorithmn")
    hashing.add_argument('--sha256', action="store_true", help="Use sha256 hash algorithmn")
    hashing.add_argument('--sha512', action="store_true", help="Use sha512 hash algorithmn")
    hashing.add_argument('--md5', action="store_true", help="Use md5 hash algorithmn")

    encryption = parser.add_argument_group(title='Encryption')
    encryption.add_argument('--rot13', action="store_true", help="Encryption Caesar")
    encryption.add_argument('--xor', action="store_true", help="Encryption xor")
    encryption.add_argument('--key', required='--xor' in sys.argv, metavar='KEY', help="Key for encryption")

    optional = parser.add_argument_group(title='Other')
    optional.add_argument('--clip', action="store_true", help="Copy to clipboard")
    optional.add_argument('--upper', action="store_true", help="View the result with uppercase")
    optional.add_argument('--view', action="store_true", help="View result")
    optional.add_argument('--verbose', action='store_true', help="Mode verbose")
    optional.add_argument('--debug', action='store_true', help="Mode debug")

    args = parser.parse_args()

    return args

def action(mode):

    # Input
    if mode.text is not None:
        
        data = mode.text.encode('utf8')
       
    elif mode.file is not None:

        data = tools.readb(mode.file)

    # Hashing
    if mode.sha1:
        result = hashing.sha1(data)
    
    if mode.sha256:
        result = hashing.sha256(data)

    if mode.sha512:
        result = hashing.sha512(data)
    
    if mode.md5:
        result = hashing.md5(data)
    
    # Encoding
    if mode.b16:
        result = encoding.b16(data)
    
    if mode.b32:
        result = encoding.b32(data)

    if mode.b64:
        result = encoding.b64(data)
    
    # Encryption
    if mode.rot13:
        result = encryption.Shift_Cipher().ascii_letter(data, 13, 1)
    
    if mode.xor:
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
        tools.writeb(result, mode.output)

def main():

    # Init Logger
    logger = logging.getLogger()
    logging.basicConfig(format='%(levelname)s :: %(message)s')

    args = check_args(sys.argv[1:])

    # Run
    action(args)


if __name__ == "__main__":

    main()
