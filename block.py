import hashlib
import time

class Block:
    def _init_(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        data_to_hash = (str(self.index) + str(self.timestamp) +
                        str(self.data) + str(self.previous_hash))
        return hashlib.sha256(data_to_hash.encode()).hexdigest()

class Blockchain:
    def _init_(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, time.time(), "Genesis Block", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, data):
        latest_block = self.get_latest_block()
        new_block = Block(len(self.chain), time.time(), data, latest_block.hash)
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True

# Example Usage
if _name_ == "_main_":
    skillhive_chain = Blockchain()

    # Adding blocks for user credentials
    skillhive_chain.add_block({"user": "Alice", "credential": "Certified Data Analyst"})
    skillhive_chain.add_block({"user": "Bob", "credential": "Full Stack Developer"})
    skillhive_chain.add_block({"user": "Charlie", "credential": "AI Specialist"})

    # Display the blockchain
    for block in skillhive_chain.chain:
        print(f"Block {block.index}:\nData: {block.data}\nHash: {block.hash}\n")

    # Validate the blockchain
    print("Blockchain valid:", skillhive_chain.is_chain_valid())
