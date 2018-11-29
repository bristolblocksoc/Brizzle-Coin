import ecdsa
import flask
from datetime import time
from hashlib import sha256
import bitarray

import utils

class Block():
    '''
    The main blockchain class.
    '''
    def __init__(self, index, previousHash, timestamp, data):
        self.index = index
        self.previousHash = previousHash
        self.timestamp = timestamp
        self.data = data

    def calculateHash(self):
        '''
        Calculate the hash.
        '''
        m = sha256()

        b = bitarray.bitarray()
        m.update(utils.strbin(str(self.index)))
        m.update(utils.strbin(self.previousHash))
        m.update(utils.strbin(str(self.timestamp)))
        m.update(utils.strbin(self.data))

        return m.hexdigest()

    def __str__(self):
        return self.calculateHash()



if __name__ == '__main__':
    genesisBlock = Block(0, '816534932c2b7154836da6afc367695e6337db8a921823784c14378abed4f7d7', None, "the genesis block")
    print(genesisBlock);
