from web3 import Web3

# Ethereum RPC URL
eth_rpc_url = "https://eth.llamarpc.com"

# Function to check balance on a specific network
def check_balance(network_rpc_url, network_name, address, output_file):
    w3 = Web3(Web3.HTTPProvider(network_rpc_url))
    balance_wei = w3.eth.get_balance(address)
    balance = w3.from_wei(balance_wei, 'ether')
    print(f"Address: {address}")
    print(f"{network_name} Balance: {balance} {network_name}")
    
    # Check if balance is greater than 0
    if balance > 0:
        # Open the output file in append mode and write the address
        with open(output_file, "a") as file:
            file.write(address + "\n")
            print(f"Non-zero balance found. Address saved to '{output_file}'")

# File path for the input dataset of wallet addresses
input_file = r"C:\Users\oluwa\OneDrive\Documents\my files\public keys5.txt"

# File to save addresses with non-zero balances
output_file = r"C:\Users\oluwa\OneDrive\Documents\my files\nonzero5.txt"

# Open the input file in read mode
with open(input_file, "r") as file:
    # Read the addresses from the file
    addresses = file.read().splitlines()

# Iterate over each address in the dataset
for address in addresses:
    check_balance(eth_rpc_url, "Ethereum", address, output_file)

# Print a message indicating the process is complete
print("All addresses checked. Wallets with non-zero balances saved to 'nonzero.txt'")
