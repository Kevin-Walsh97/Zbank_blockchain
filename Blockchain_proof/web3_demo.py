from web3 import Web3
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))

latest_block = w3.eth.blockNumber
print(latest_block)
balance_node1 = w3.eth.getBalance("0xe4EA9933Cf7aEC101d5fFEE9e25330Ea33a6cA99")
print(balance_node1)