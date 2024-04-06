from web3 import Web3
import json

# Connect to an Ethereum node (replace 'http://localhost:8545' with your node's URL)
web3 = Web3(Web3.HTTPProvider('http://localhost:8545'))

# Load the compiled contract ABI and bytecode
with open('PdfStorage.json') as f:
    contract_data = json.load(f)
contract_abi = contract_data['abi']
contract_address = '0x123...'  # Replace with the deployed contract address

# Create a contract object
contract = web3.eth.contract(address=contract_address, abi=contract_abi)

# Example: Store a PDF page
page_number = 1
hex_string = "546869730a69730a610a746573740a646f63756d656e740a77650a77696c6c0a686176650a636f6e7665727465640a746f0a68657861646563696d616c0a737472696e67732e0a53696e636572656c792c0a5468650a41666768616e0a44414f0a7465616d"
tx_hash = contract.functions.storePdf(page_number, hex_string).transact()

# Wait for the transaction to be mined
web3.eth.waitForTransactionReceipt(tx_hash)

# Example: Retrieve a PDF page
retrieved_hex_string = contract.functions.getPdf(page_number).call()
print("Retrieved Hexadecimal String:", retrieved_hex_string)
