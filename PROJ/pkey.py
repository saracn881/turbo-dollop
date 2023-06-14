import eth_keys
from mnemonic import Mnemonic

seed_phrase = "silk hundred polar blast gospel promote trick violin shallow couple leopard entire"

mnemonic = Mnemonic("english")
seed = mnemonic.to_seed(seed_phrase)

private_key_bytes = seed[:32]
private_key = eth_keys.keys.PrivateKey(private_key_bytes)

print("Ethereum Private Key:", private_key.to_hex())
