import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, knowledge, proof, timestamp=None):
        self.index = index
        self.previous_hash = previous_hash
        self.knowledge = knowledge
        self.proof = proof
        self.timestamp = timestamp or time.time()
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = f"{self.index}{self.previous_hash}{self.knowledge}{self.proof}{self.timestamp}"
        return hashlib.sha256(block_string.encode()).hexdigest()
