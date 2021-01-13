#!/usr/bin/python3
# coding : utf-8

import argparse, logging, sys
import clipboard
import hashing, encoding, encryption

def check_args(_agrs=None):
    
    # Init Argparse
    parser = argparse.ArgumentParser(description='Cryptotools')
    
    parser.add_argument('-sha1', action="store_true", help="Use sha1 hash algorithmn")
    parser.add_argument('-sha256', action="store_true", help="Use sha256 hash algorithmn")
    parser.add_argument('-sha512', action="store_true", help="Use sha512 hash algorithmn")
    parser.add_argument('-md5', action="store_true", help="Use md5 hash algorithmn")
    parser.add_argument('-b16', action="store_true", help="Encode with base 16")
    parser.add_argument('-b32', action="store_true", help="Encode with base 32")
    parser.add_argument('-b64', action="store_true", help="Encode with base 64")
    parser.add_argument('-rot13', action="store_true", help="Encryption Caesar")
    parser.add_argument('-xor', action="store_true", help="Encryption xor")
    parser.add_argument('-c', '--clip', action="store_true", help="Copy to clipboard")
    parser.add_argument('-k', '--key', type=str, metavar='key', help="Key for encryption")
    parser.add_argument('-up', '--upper', action="store_true", help="Result with uppercase")
    parser.add_argument('-hid', '--hidden', action="store_true", help="Hidden result")
    parser.add_argument('-v', '--verbose', action='store_true', help="Mode verbose")
    parser.add_argument('-d', '--debug', action='store_true', help="Mode debug")
    parser.add_argument('text', type=str, metavar='text', help="Text for Encode/Hash")

    args = parser.parse_args()
    
    return args

def action(mode):

    if mode.sha1:
        result = hashing.sha1(mode.text)
    
    if mode.sha256:
        result = hashing.sha256(mode.text)

    if mode.sha512:
        result = hashing.sha512(mode.text)
    
    if mode.md5:
        result = hashing.md5(mode.text)

    if mode.b16:
        result = encoding.b16(mode.text)
    
    if mode.b32:
        result = encoding.b32(mode.text)

    if mode.b64:
        result = encoding.b64(mode.text)

    if mode.rot13:
        result = encryption.Shift_Cipher().ascii_letter(mode.text, 13, 1)
    
    if mode.xor:
        result = encryption.Xor_Cipher().str(mode.text, mode.key)

    # Uppercase
    if mode.upper:
        result = result.upper()

    # View result
    if not mode.hidden:
        print(result)

    # Copy result
    if mode.clip:
        clipboard.copy(result)

def main():

    # Init Logger
    logger = logging.getLogger()
    logging.basicConfig(format='%(levelname)s :: %(message)s')

    args = check_args(sys.argv[1:])

    # Run
    action(args)


if __name__ == "__main__":

    main()
