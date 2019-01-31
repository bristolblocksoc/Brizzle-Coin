import ecdsa
import flask
from hashlib import sha256
import time

import utils

class Block():
    """
    The main blockchain class.
    """
    def __init__(self, index, previous_hash, timestamp, data):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data

    def calculate_hash(self):
        '''
        Calculate the hash.
        '''
        m = sha256()

        m.update(str(self.index).encode("utf-8"))
        m.update(self.previous_hash.encode("utf-8"))
        m.update(str(self.timestamp).encode("utf-8"))
        m.update(self.data.encode("utf-8"))

        return m.hexdigest()

    def __str__(self):
        return self.calculate_hash()

def generate_next_block(block_data, previous_block):
    next_index = previous_block.index + 1
    next_timestamp = time.time()
    previous_hash = previous_block.calculate_hash()
    
    return Block(next_index, previous_hash, next_timestamp, block_data)

def is_valid_new_block(new_block, previous_block):
    if previous_block.index + 1 != new_block.index:
        print('invalid index')

        return False
    elif previous_block.calculate_hash() != new_block.previous_hash:
        print('invalid previous hash')

        return False

    return True

def is_valid_chain(blockchain):
    is_valid_genesis = blockchain[0].calculate_hash() == genesis_block.calculate_hash()

    for i in range(1, len(blockchain)):
        if not is_valid_new_block(blockchain[i], blockchain[i - 1]):
            return False

    return True

def get_longest_chain(old_blockchain, new_blockchain):
    if len(new_blockchain) > len(old_blockchain):
        return new_blockchain

    return old_blockchain

genesis_block = Block(0, '816534932c2b7154836da6afc367695e6337db8a921823784c14378abed4f7d7', None, "the genesis block")

if __name__ == '__main__':
    next_block = generate_next_block("wow", genesis_block)

    blockchain = [genesis_block]
    blockchain = get_longest_chain(blockchain, [genesis_block, next_block])

    print(genesis_block);
    print(next_block);

    print(blockchain)
