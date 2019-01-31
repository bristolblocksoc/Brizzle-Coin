import ecdsa
import flask
from datetime import time
from hashlib import sha256

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

        m.update(str(self.index).encode("utf-8"))
        m.update(self.previousHash.encode("utf-8"))
        m.update(str(self.timestamp).encode("utf-8"))
        m.update(self.data.encode("utf-8"))

        return m.hexdigest()

    def __str__(self):
        return self.calculateHash()



if __name__ == '__main__':
    genesisBlock = Block(0, '816534932c2b7154836da6afc367695e6337db8a921823784c14378abed4f7d7', None, "the genesis block")
    print(genesisBlock);
