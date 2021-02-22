#!/usr/bin/python3
# coding : utf-8

import argparse, logging, sys
import clipboard
from functions import args 

def check_args(_agrs=None):
    
    # Init Argparse
    parser = argparse.ArgumentParser(description='Cryptotools')

    typeGroup = parser.add_mutually_exclusive_group()
    typeGroup.add_argument('-t', '--text', metavar='TEXT', help="Text for Encode/Hash/Encrypt")
    typeGroup.add_argument('-f', '--file', metavar='FILE', help="File for Encode/Hash/Encrypt")
    parser.add_argument('-o', '--output', metavar='OUTPUT', help="File output")

    encoding = parser.add_argument_group(title='Encoding')
    encoding.add_argument('-b16', '--base16', action="store_true", help="Encode with base 16")
    encoding.add_argument('-b32', '--base32', action="store_true", help="Encode with base 32")
    encoding.add_argument('-b64', '--base64', action="store_true", help="Encode with base 64")

    hashing = parser.add_argument_group(title='Hashing')
    hashing.add_argument('-sha1', '--sha1', action="store_true", help="Use sha1 hash algorithmn")
    hashing.add_argument('-sha256', '--sha256', action="store_true", help="Use sha256 hash algorithmn")
    hashing.add_argument('-sha512', '--sha512', action="store_true", help="Use sha512 hash algorithmn")
    hashing.add_argument('-md5', '--md5', action="store_true", help="Use md5 hash algorithmn")
    hashing.add_argument('-test', '--test', action="store_true", help="Test hashing")

    encryption = parser.add_argument_group(title='Encryption')
    encryption.add_argument('-rot13', '--rot13', action="store_true", help="Encryption ROT13")
    encryption.add_argument('-caesar', '--caesar', metavar='TYPE', choices=['letter', 'ascii'], help="Encryption Caesar (Select letter or ascii)")
    encryption.add_argument('-vigenere', '--vigenere', metavar='TYPE', choices=['letter', 'ascii'], help="Encryption Vigenere (Select letter or ascii)")
    encryption.add_argument('-xor', '--xor', action="store_true", help="Encryption xor")

    encryption_sub = parser.add_argument_group(title='Encryption - Sub args')
    encryption_sub.add_argument('-k', '--key', metavar='KEY', help="Key for encryption")
    encryption_sub.add_argument('-shift', '--shift', metavar='NUMBER', type=int, help="Number for shift")
    encryption_sub.add_argument('-repeat', '--repeat', metavar='NUMBER', type=int, default=1, help="Number for repetition shift")

    optional = parser.add_argument_group(title='Other')
    optional.add_argument('-c', '--clip', action="store_true", help="Copy to clipboard")
    optional.add_argument('-up', '--upper', action="store_true", help="View the result with uppercase")
    optional.add_argument('-v', '--view', action="store_true", help="View result")
    optional.add_argument('-vv', '--verbose', action='store_true', help="Mode verbose")
    optional.add_argument('-d', '--debug', action='store_true', help="Mode debug")

    args = parser.parse_args()

    return args

def main():

    sysargs = check_args(sys.argv[1:])

    # Init Logger
    logger = logging.getLogger()
    logging.basicConfig(format='%(levelname)s :: %(message)s')

    if sysargs.verbose:
        logger.setLevel(logging.INFO)
    if sysargs.debug:
        logger.setLevel(logging.DEBUG)

    # Run
    args.action(sysargs)


if __name__ == "__main__":

    main()
