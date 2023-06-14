import random
from mnemonic import Mnemonic
from eth_account import Account
from web3 import Web3
import asyncio

output_file = r"C:\Users\oluwa\OneDrive\Documents\my files\output3.txt"  # Replace with the desired output file path

# Ethereum RPC URLs
eth_rpc_urls = [
     "https://eth.llamarpc.com"
]

# Number of seed phrases to generate in each batch
batch_size = 100

# Number of batches to process
num_batches = 100

def generate_seed_phrase():
    mnemo = Mnemonic("english")
    seed_phrase = mnemo.generate(strength=128)
    return seed_phrase

async def generate_public_key_from_seed_phrase(seed_phrase):
    Account.enable_unaudited_hdwallet_features()
    account = Account.from_mnemonic(seed_phrase)
    address = account.address
    return address, account.key

async def check_balance(network_rpc_url, network_name, address, seed_phrase, public_key):
    w3 = Web3(Web3.HTTPProvider(network_rpc_url))
    balance_wei = w3.eth.get_balance(address)
    balance = w3.from_wei(balance_wei, 'ether')
    print(f"Address: {address}")
    print(f"{network_name} Balance: {balance} {network_name}")

    # Check if balance is greater than 0
    if balance > 0:
        # Open the output file in append mode and write the seed phrase, address, public key, and balance
        with open(output_file, "a+") as file:
            file.write(f"Seed Phrase: {seed_phrase}\n")
            file.write(f"Address: {address}\n")
            file.write(f"Public Key: {public_key}\n")
            file.write(f"Balance: {balance} {network_name}\n")
            file.write("-------------------\n")
            file.flush()  # Flush the file to ensure immediate saving
            print(f"Non-zero balance found. Seed Phrase, Address, Public Key, and Balance saved to '{output_file}'")

async def process_batch(batch, rpc_urls):
    tasks = []
    for seed_phrase in batch:
        public_key = await generate_public_key_from_seed_phrase(seed_phrase)
        tasks.append(check_balance(random.choice(rpc_urls), "Ethereum", public_key[0], seed_phrase, public_key[1]))
    await asyncio.gather(*tasks)

async def process_addresses():
    # Generate seed phrases in batches
    for _ in range(num_batches):
        batch = [generate_seed_phrase() for _ in range(batch_size)]
        await process_batch(batch, eth_rpc_urls)

# Run the address processing asynchronously
asyncio.run(process_addresses())
