#!/usr/bin/python3
# coding : utf-8


def read(file):

    with open(file, 'rb') as file:
        return file.read()


def write(data, file):

    with open(file, 'wb') as file:
        file.write(data)
