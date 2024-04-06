from web3 import Web3
import json

# Load the contract ABI from the JSON file
with open('PdfStorage.json') as f:
    contract_abi = json.load(f)

# Connect to the Ethereum Mainnet using Infura
infura_url = 'https://mainnet.infura.io/v3/fa76bd4e09dc4ed4b565d0faf04a13e9'
web3 = Web3(Web3.HTTPProvider(infura_url))

# Convert the contract address to checksum format
contract_address = web3.to_checksum_address('0x728e2be53247bb626510de271b7c3e65bfb6fda3')

# Create a contract object
contract = web3.eth.contract(address=contract_address, abi=contract_abi)

# Example: Call the 'getPdf' function of the contract
page_number = 1  # Adjust the page number as needed
pdf_data = contract.functions.getPdf(page_number).call()

print("PDF Data:", pdf_data)
