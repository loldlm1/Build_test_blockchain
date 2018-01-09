import hashlib
import json

from time import time
from uuid import uuid4

class Blockchain(object):
  def __init__(self):
    self.chain = []
    self.current_transactions = []

    # Creates the genesis block
    self.new_block(previous_hash = 1, proof = 100)

  def new_block(self, proof, previous_hash = None):
    block = {
      'index': len(self.chain) + 1,
      'timestamp': time(),
      'transactions': self.current_transactions,
      'proof': proof,
      'previous_hash': previous_hash or self.hash(self.chain[-1])
    }

    # Resets the current_list of transactions
    self.current_transactions = []

    # Append the block to the chain array
    self.chain.append(block)
    return block

  def new_transaction(self, sender, recipient, amount):
    # Adds a new transaction to the list of transactions
    self.current_transactions.append({
      'sender': sender,
      'recipient': recipient,
      'amount': amount,
    })

    # The index of the Block that will hold this transaction
    return self.last_block['index'] + 1

  def proof_of_work(self, last_proof):
    # Personal test proof of work Algorithm:
    #  - Find a number p_old such that hash(pp_old) contains 0 at beginning and 1 at end, where p is the previous p_old
    proof = 0
    while self.valid_proof(last_proof, proof) is False:
      proof += 1

  @staticmethod
  def valid_proof(last_proof, proof):
    # Validates the Proof: Does hash(last_proof, proof) contain 0 at beginning and 1 at end?
    guess = f'{last_proof}{proof}'.encode()
    guess_hash = hashlib.sha256(guess).hexdigest()
    return guess_hash[0] == '0' and guess_hash[-1] == '1'

  @staticmethod
  def hash(block):
    block_string = json.dumps(block, sort_keys = True).encode()
    return hashlib.sha256(block_string).hexdigest()

  @property
  def last_block(self):
    return self.chain[-1]

block = Blockchain()
print(block.proof_of_work(1))
