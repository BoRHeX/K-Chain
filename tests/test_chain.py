import unittest
from src.blockchain.chain import KnowledgeChain
from src.blockchain.consensus import ProofOfKnowledge

class TestKnowledgeChain(unittest.TestCase):
    def setUp(self):
        self.chain = KnowledgeChain()
        self.pok = ProofOfKnowledge()

    def test_genesis_block(self):
        self.assertEqual(self.chain.get_last_block().knowledge, "Genesis Block")

    def test_knowledge_validation(self):
        self.pok.vote("user1", "knowledge1", True)
        self.assertTrue(self.pok.validate_knowledge("knowledge1"))

    def test_kbc_balance(self):
        self.chain.kbc_balance = {"user1": 0.5, "user2": 0.5}
        self.chain.balance_kbc()
        self.assertEqual(sum(self.chain.kbc_balance.values()), 1)

if __name__ == '__main__':
    unittest.main()
