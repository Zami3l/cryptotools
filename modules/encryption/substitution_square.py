#!/usr/bin/python3
# coding : utf-8

import logging
import numpy

class Substitution_Square():

    # Generate the table square Polybe
    def generate_array_square(self, key):

        letter = b'abcdefghijklmnopqrstuvxyz'
        squareArray = numpy.zeros((5,5), dtype=int)

        for iKey in key+letter:

            nextKey = False

            for iRow in range(5):

                for iColumn in range(5):

                    if squareArray[iRow, iColumn]:

                        if squareArray[iRow, iColumn] == iKey:
                            nextKey = True
                            break
                        
                    else:

                        squareArray[iRow, iColumn] = iKey
                        nextKey = True
                        break

                if nextKey:
                    break

        return squareArray

    # Function checks if the char is a number in the ascii table
    def check_number(self, text):

        if text > 47 and text < 58:
            return True
        else:
            return False

    def ascii_letter(self, mode, permutation, plainText, key):

        squareArray = numpy.array(self.generate_array_square(key))
        cipherText = bytearray()
        nextPass = False

        for iNum, iText in enumerate(plainText):

            if mode == 'E':

                tmp = numpy.argwhere(squareArray == iText)

                if tmp.any():

                    # Permutatation row and column
                    if not permutation:

                        cipherText.append(ord(str(tmp[0, 0] + 1)))
                        cipherText.append(ord(str(tmp[0, 1] + 1)))

                    else:

                        cipherText.append(ord(str(tmp[0, 1] + 1)))
                        cipherText.append(ord(str(tmp[0, 0] + 1)))

                # If the char is special
                else:

                    cipherText.append(iText)

            if mode == 'D':
                
                # True when the char is used pairs
                # First is row, Second is column
                if nextPass :
                    nextPass = False
                    continue

                if self.check_number(iText):

                    row = int(chr(iText)) - 1
                    column = int(chr(plainText[iNum + 1])) - 1
                    
                    # Permutatation row and column
                    if not permutation:

                        cipherText.append(squareArray[row, column])

                    else:

                        cipherText.append(squareArray[column, row])

                    nextPass = True

                # If the char is special
                else:

                    cipherText.append(iText)

        return cipherText
