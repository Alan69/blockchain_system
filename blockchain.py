import hashlib
import json
import time
import requests
from uuid import uuid4
from urllib.parse import urlparse

class Block:
    def __init__(self, index, timestamp, transactions, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = json.dumps({
            "index": self.index,
            "timestamp": self.timestamp,
            "transactions": self.transactions,
            "previous_hash": self.previous_hash,
            "nonce": self.nonce
        }, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def mine_block(self, difficulty):
        while self.hash[:difficulty] != "0" * difficulty:
            self.nonce += 1
            self.hash = self.calculate_hash()

    def __str__(self):
        return f"Block #{self.index} [{self.timestamp}] - Hash: {self.hash}"

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 2
        self.pending_transactions = []
        self.nodes = set()

    def create_genesis_block(self):
        return Block(0, time.time(), [], "0")

    def register_node(self, address):
        parsed_url = urlparse(address)
        self.nodes.add(parsed_url.netloc)

    def consensus(self):
        network = self.nodes
        longest_chain = None
        max_length = len(self.chain)

        for node in network:
            response = requests.get(f'http://{node}/chain')

            if response.status_code == 200:
                length = response.json()['length']
                chain = response.json()['chain']

                if length > max_length and self.is_chain_valid(chain):
                    max_length = length
                    longest_chain = chain

        if longest_chain:
            self.chain = longest_chain
            return True

        return False

    def get_latest_block(self):
        return self.chain[-1]

    def add_transaction(self, sender, recipient, amount):
        self.pending_transactions.append({
            "sender": sender,
            "recipient": recipient,
            "amount": amount
        })

    def mine_pending_transactions(self, miner):
        block = Block(len(self.chain), time.time(), self.pending_transactions, self.get_latest_block().hash)
        block.mine_block(self.difficulty)
        print("Block mined:", block)
        self.chain.append(block)
        self.pending_transactions = [{"sender": "system", "recipient": miner, "amount": 1}]

    def is_chain_valid(self, chain=None):
        if not chain:
            chain = self.chain

        for i in range(1, len(chain)):
            current_block = chain[i]
            previous_block = chain[i - 1]

            if current_block.hash != current_block.calculate_hash():
                return False

            if current_block.previous_hash != previous_block.hash:
                return False

        return True

# Example usage
if __name__ == "__main__":
    blockchain = Blockchain()
    blockchain.register_node("http://localhost:5000")

    blockchain.add_transaction("Alice", "Bob", 5)
    blockchain.add_transaction("Bob", "Charlie", 10)

    blockchain.mine_pending_transactions("miner")

    blockchain.add_transaction("Alice", "Charlie", 7)
    blockchain.mine_pending_transactions("miner")

    print("Chain is valid:", blockchain.is_chain_valid())

    blockchain.consensus()
