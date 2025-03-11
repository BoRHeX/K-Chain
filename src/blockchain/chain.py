from .block import Block

class KnowledgeChain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.kbc_balance = {}

    def create_genesis_block(self):
        return Block(0, "0", "Genesis Block", 0)

    def get_last_block(self):
        return self.chain[-1]

    def add_block(self, knowledge, proof):
        last_block = self.get_last_block()
        new_block = Block(len(self.chain), last_block.hash, knowledge, proof)
        self.chain.append(new_block)
        self.balance_kbc()

    def balance_kbc(self):
        total_kbc = sum(self.kbc_balance.values())
        if total_kbc != 1:
            for user in self.kbc_balance:
                self.kbc_balance[user] /= total_kbc
