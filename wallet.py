import binascii
from ecdsa.ecdsa import generator_secp256k1
from pycoin.ecdsa.secp256k1 import secp256k1_generator
from pycoin.encoding import b58
import secrets
import hashlib


def double_sha256(x):
    return hashlib.sha256(hashlib.sha256(binascii.unhexlify(x)).digest()).hexdigest()


def hash160(x):
    return hashlib.new('ripemd160', hashlib.sha256(binascii.unhexlify(x)).digest()).hexdigest()


def get_privKey():
    return secrets.randbelow(generator_secp256k1.order())


def get_hex(privKey):
    return '%064x' % privKey


def get_wif(hex):
    data = '80' + hex + '01'
    checksum = double_sha256(data)[:8]
    data = data + checksum
    wif = b58.b2a_base58(binascii.unhexlify(data))
    return wif


def get_pubKey(privKey):
    G = secp256k1_generator
    Point = privKey * G
    return Point


def get_pubKey_compressed(Point):
    # Compressed (prefix 02 if y is even, 03 if y is odd)
    x = '%064x' % Point[0]
    pubKey = ('02' if Point[1] % 2 == 0 else '03') + x
    return pubKey


def get_pubKey_uncompressed(Point):
    x = '%064x' % Point[0]
    y = '%064x' % Point[1]
    pubKey = '04' + x + y
    return pubKey


def get_adress(pubKey):
    hash = hashlib.new('ripemd160', hashlib.sha256(binascii.unhexlify(pubKey)).digest()).hexdigest()
    data = '00' + hash
    checksum = double_sha256(data)[:8]
    data = data + checksum
    address = b58.b2a_base58(binascii.unhexlify(data))
    return address
