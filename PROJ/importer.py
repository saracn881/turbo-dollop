from eth_account import Account
import sys

def generate_public_key_from_seed_phrase(seed_phrase):
    Account.enable_unaudited_hdwallet_features()
    account = Account.from_mnemonic(seed_phrase)
    address = account.address
    return address

# Path to the local data set file
data_set_file = r"C:\Users\oluwa\OneDrive\Documents\my files\1.txt"

# Read seed phrases from the data set file
with open(data_set_file, "r") as file:
    seed_phrases = file.read().splitlines()

# Generate public keys (Ethereum addresses) for each seed phrase
public_keys = []
total_seed_phrases = len(seed_phrases)

for i, seed_phrase in enumerate(seed_phrases):
    public_key = generate_public_key_from_seed_phrase(seed_phrase)
    public_keys.append(public_key)

    # Calculate progress percentage
    progress = (i + 1) / total_seed_phrases * 100

    # Update progress on the terminal
    sys.stdout.write("\rProgress: %.2f%%" % progress)
    sys.stdout.flush()

# Save the public keys to a text file
output_file = r"C:\Users\oluwa\OneDrive\Documents\my files\public keys.txt"
with open(output_file, "w") as file:
    for public_key in public_keys:
        file.write(public_key + "\n")

# Print completion message
print("\nPublic keys saved to", output_file)
