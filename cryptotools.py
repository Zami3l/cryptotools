#!/usr/bin/python3
# coding : utf-8

import argparse, logging, sys
import clipboard
from functions import args

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
    hashing.add_argument('--test', action="store_true", help="Test hashing")

    encryption = parser.add_argument_group(title='Encryption')
    encryption.add_argument('--rot13', action="store_true", help="Encryption ROT13")
    encryption.add_argument('--caesar', action="store_true", help="Encryption Caesar")
    encryption.add_argument('--xor', action="store_true", help="Encryption xor")

    encryption.add_argument('--key', metavar='KEY', help="Key for encryption")
    encryption.add_argument('--shift', metavar='NUMBER', type=int, help="Number for shift")

    optional = parser.add_argument_group(title='Other')
    optional.add_argument('--clip', action="store_true", help="Copy to clipboard")
    optional.add_argument('--upper', action="store_true", help="View the result with uppercase")
    optional.add_argument('--view', action="store_true", help="View result")
    optional.add_argument('--verbose', action='store_true', help="Mode verbose")
    optional.add_argument('--debug', action='store_true', help="Mode debug")

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
