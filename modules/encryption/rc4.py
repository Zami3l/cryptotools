#!/usr/bin/python3
# coding : utf-8

import logging

class RC4():

    nbIterations = 256

    #Key Scheduling Algorithm
    def KSA(self, key):

        #Init
        S = list(range(self.nbIterations))
        j = 0
        keySize = len(key)

        for i in range(self.nbIterations):

            j = (j + S[i] + key[i % keySize]) % self.nbIterations
            S[i], S[j] = S[j], S[i] #Swap i and j

        return S

    #Pseudo-random generation algorithm
    def PRGA(self, S):

        #Init
        i = 0
        j = 0

        while True:

            i = (i + 1) % self.nbIterations
            j = (j + S[i]) % self.nbIterations
            S[i], S[j] = S[j], S[i] #Swap i and j
            K = S[(S[i] + S[j]) % self.nbIterations]

            yield K

    def cipher(self, mode, plainText, key):

        keystream = self.PRGA(self.KSA(key))
        result = bytearray()

        for index in plainText:

            result.append(index ^ next(keystream))

        return result
