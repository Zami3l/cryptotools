#!/usr/bin/python3
# coding : utf-8

import logging

def read(file):

    with open(file, 'rb') as file:

        fileRead = file.read()
        logging.debug('\n===READ FILE===\n%s\n===============', fileRead)

        return fileRead

def write(data, file):

    with open(file, 'wb') as file:

        logging.debug('\n===WRITE FILE===\n%s\n================', data)
        file.write(data)
