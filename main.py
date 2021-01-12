#!/usr/bin/python3
# coding : utf-8

import argparse, logging, sys
import clipboard
import hashing, encoding

def check_args(_agrs=None):
    
    # Init Argparse
    parser = argparse.ArgumentParser(description='Hashtools')
    
    parser.add_argument('-v', '--verbose', action='store_true', help="Mode verbose")
    parser.add_argument('-d', '--debug', action='store_true', help="Mode debug")
    parser.add_argument('-sha1', '--sha1', action="store_true", help="Use sha1 hash algorithmn")
    parser.add_argument('-sha256', '--sha256', action="store_true", help="Use sha256 hash algorithmn")
    parser.add_argument('-sha512', '--sha512', action="store_true", help="Use sha512 hash algorithmn")
    parser.add_argument('-b16', '--b16', action="store_true", help="Encode with base 16")
    parser.add_argument('-b32', '--b32', action="store_true", help="Encode with base 32")
    parser.add_argument('-b64', '--b64', action="store_true", help="Encode with base 64")
    parser.add_argument('text', type=str, metavar='text', help="Text for Encode/Hash")
    parser.add_argument('-c', '--clip', action="store_true", help="Copy to clipboard")

    args = parser.parse_args()
    
    return args

def action(mode):

    if mode.sha1:
        result = hashing.sha1(mode.text)
    
    if mode.sha256:
        result = hashing.sha256(mode.text)

    if mode.sha512:
        result = hashing.sha512(mode.text)
    
    if mode.b16:
        result = encoding.b16(mode.text)
    
    if mode.b32:
        result = encoding.b32(mode.text)

    if mode.b64:
        result = encoding.b64(mode.text)

    return result

def main():

    # Init Logger
    logger = logging.getLogger()
    logging.basicConfig(format='%(levelname)s :: %(message)s')

    args = check_args(sys.argv[1:])

    # Return
    result = action(args)

    # View result
    print(result)

    # Copy result
    if args.clip:
        clipboard.copy(result)

if __name__ == "__main__":

    main()
