class ProofOfKnowledge:
    def __init__(self):
        self.votes = {}

    def vote(self, user, knowledge, is_valid):
        if knowledge not in self.votes:
            self.votes[knowledge] = []
        self.votes[knowledge].append((user, is_valid))

    def validate_knowledge(self, knowledge):
        votes = self.votes.get(knowledge, [])
        positive_votes = sum(1 for _, is_valid in votes if is_valid)
        return positive_votes > len(votes) / 2
