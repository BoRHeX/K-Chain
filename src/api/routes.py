import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from flask import Flask, request, jsonify
from src.blockchain.chain import KnowledgeChain
from src.blockchain.consensus import ProofOfKnowledge

app = Flask(__name__)
knowledge_chain = KnowledgeChain()
proof_of_knowledge = ProofOfKnowledge()

@app.route('/register', methods=['POST'])
def register():
    user = request.json['user']
    knowledge_chain.kbc_balance[user] = 0
    return jsonify({"message": "User registered successfully"}), 201

@app.route('/submit_knowledge', methods=['POST'])
def submit_knowledge():
    user = request.json['user']
    knowledge = request.json['knowledge']
    proof = request.json['proof']
    if proof_of_knowledge.validate_knowledge(knowledge):
        knowledge_chain.add_block(knowledge, proof)
        knowledge_chain.kbc_balance[user] += 0.1  # Example increment
        return jsonify({"message": "Knowledge submitted successfully"}), 201
    return jsonify({"message": "Knowledge validation failed"}), 400

@app.route('/balance', methods=['GET'])
def balance():
    user = request.args.get('user')
    balance = knowledge_chain.kbc_balance.get(user, 0)
    return jsonify({"balance": balance}), 200

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
