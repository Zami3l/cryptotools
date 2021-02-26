#!/usr/bin/python3
# coding : utf-8

import hashlib
import toml

class Sha_Custom:
    
    def __init__(self, fileConf):
        self.param = toml.load(fileConf)

    def hashing(self, input):
        return hashlib.sha3_256(input).hexdigest() # Hash SHA3-256

    def ror(self, input, positionCut, orderRor):

        index, rank, output = 0, list(), list() 

        while index < len(input): # Cut 

            rank.append(input[0 + index:positionCut + index])
            index += positionCut

        index = 0

        while index < len(rank): # Ror

            output.append(rank[orderRor[index]])
            index += 1

        return ''.join(output)

    def replace(self, input, listing, firstList, secondList):

        index, output, save = 0, list(), [0]*len(firstList)

        while index < len(input): # Search and replace

            position, found = 0, False 
            
            # Search
            while found == False: 

                if input[index] == listing[position]:
                    found = True
                    save[position] += 1
                else:
                    position += 1
                    
            # Replace
            if save[position] < 2: # If the char has been remplaced < 2, use firstList 
                output.append(firstList[position])
            elif save[position] == 2: 
                output.append(secondList[position])
                save[position] = 0

            index += 1

        return ''.join(output) 

    def exec(self, plainText):

        cipherText = self.hashing(plainText)
        cipherText = self.ror(cipherText, 5, self.param['ror']['1'])
        cipherText = self.replace(cipherText, self.param['order']['1'], self.param['disorder']['1'], self.param['disorder']['2'])
        cipherText = self.ror(cipherText, 5, self.param['ror']['2'])

        return cipherText.encode('utf8')

