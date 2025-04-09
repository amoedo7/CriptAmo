# backend/wallet_utils.py
import os, ecdsa, hashlib, base58

def generate_private_key():
    return os.urandom(32).hex()

def private_to_public_key(priv_key_hex):
    sk = ecdsa.SigningKey.from_string(bytes.fromhex(priv_key_hex), curve=ecdsa.SECP256k1)
    vk = sk.get_verifying_key()
    return b'\x04' + vk.to_string()

def ripemd160(data):
    return hashlib.new('ripemd160', data).digest()

def base58_address(prefix, pub_key_hash):
    payload = prefix + pub_key_hash
    checksum = hashlib.sha256(hashlib.sha256(payload).digest()).digest()[:4]
    return base58.b58encode(payload + checksum).decode()

def generate_addresses(pub_key):
    pub_key_sha = hashlib.sha256(pub_key).digest()
    pub_key_ripemd = ripemd160(pub_key_sha)

    addresses = {
        "Bitcoin": base58_address(b'\x00', pub_key_ripemd),
        "Litecoin": base58_address(b'\x30', pub_key_ripemd),
        "Dogecoin": base58_address(b'\x1e', pub_key_ripemd),
        "BitcoinCash": base58_address(b'\x00', pub_key_ripemd),
        "Dash": base58_address(b'\x4c', pub_key_ripemd),
        "Clams": base58_address(b'\x89', pub_key_ripemd),
        "Zcash": base58_address(b'\x1c\xb8', pub_key_ripemd),
    }

    eth_hash = hashlib.new('sha3_256', pub_key[1:]).digest()
    eth_address = "0x" + eth_hash[-20:].hex()
    addresses["Ethereum"] = eth_address
    addresses["BNB"] = eth_address

    return addresses
