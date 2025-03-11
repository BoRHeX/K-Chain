import json

def save_blockchain(chain, filename):
    with open(filename, 'w') as f:
        json.dump([block.__dict__ for block in chain], f)

def load_blockchain(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
        return [Block(**block) for block in data]
