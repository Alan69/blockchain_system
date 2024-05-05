# Simple Blockchain System in Python

This project implements a simple blockchain system in Python, demonstrating the basic principles of blockchain technology. The blockchain system includes features such as block creation, transaction management, proof-of-work mining, peer-to-peer networking, and consensus resolution.

## Features

- **Block Creation**: Create blocks containing transactions and previous block references.
- **Transaction Management**: Add transactions to the blockchain.
- **Proof-of-Work Mining**: Mine blocks by finding nonce values that meet the difficulty target.
- **Peer-to-Peer Networking**: Register nodes in the network and resolve chain conflicts through consensus.
- **Persistence**: Save and load the blockchain from disk for persistence.

## Getting Started

To use the blockchain system, follow these steps:

1. Clone this repository to your local machine:

    ```
    git clone https://github.com/Alan69/blockchain_system.git
    ```

2. Navigate to the project directory:

    ```
    cd blockchain_system
    ```

3. Install the required dependencies:

    ```
    pip install -r requirements.txt
    ```

4. Run the blockchain system using Python:

    ```
    python blockchain.py
    ```

5. Follow the on-screen instructions to interact with the blockchain system, such as adding transactions, mining blocks, and resolving chain conflicts.

## Usage

- **Adding Transactions**: Use the `add_transaction` method to add transactions to the blockchain.
- **Mining Blocks**: Use the `mine_pending_transactions` method to mine blocks containing pending transactions.
- **Peer-to-Peer Networking**: Register nodes in the network using the `register_node` method and resolve chain conflicts using the `consensus` method.
- **Persistence**: Save the blockchain to disk using the `save_chain` method and load it using the `load_chain` method.

## Examples

```python
# Initialize the blockchain
blockchain = Blockchain()

# Register nodes in the network
blockchain.register_node("http://localhost:5000")

# Add transactions
blockchain.add_transaction("Alice", "Bob", 5)
blockchain.add_transaction("Bob", "Charlie", 10)

# Mine pending transactions
blockchain.mine_pending_transactions("miner")

# Resolve chain conflicts
blockchain.consensus()
```

## Requirements

- Python 3.x

## Contributing

Contributions to this project are welcome! If you have any ideas, suggestions, bug reports, or feature requests, please feel free to open an issue or submit a pull request.
