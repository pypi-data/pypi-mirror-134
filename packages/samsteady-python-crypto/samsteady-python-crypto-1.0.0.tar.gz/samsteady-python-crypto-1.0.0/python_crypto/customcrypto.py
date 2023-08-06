import hashlib

from AesEverywhere import aes256
from aws_encryption_sdk.exceptions import DecryptKeyError
from awscrypto import encrypt, decrypt


def hash_value(v):
    return hashlib.sha224(bytes(v, 'utf-8')).hexdigest()

def password_encrypt(plaintext, password):
    safe_pass = password.strip()
    return aes256.encrypt(plaintext, safe_pass)

def password_decrypt(ciphertext, password):
    safe_pass = password.strip()
    return aes256.decrypt(ciphertext, safe_pass).decode("utf-8")

def _replace_in_bytes(byte_str, old, new):
    start_ind = byte_str.find(old)
    return byte_str[:start_ind] + new + byte_str[start_ind+len(old):]

def double_encrypt(plaintext, password, context={}):
    safe_pass = password.strip()
    hashed_pass = hash_value(safe_pass)
    aws_cipher = encrypt(plaintext, encryption_context={
        'pass': hashed_pass,
        **context,
    })
    stripped_cipher = _replace_in_bytes(aws_cipher, bytes(hashed_pass, 'utf-8'), b'{PASS}')
    return stripped_cipher

class BadEncryptionPassword(Exception):
    pass

def double_decrypt(stripped_ciphertext, password):
    safe_pass = password.strip()
    hashed_pass = hash_value(safe_pass)
    ciphertext = _replace_in_bytes(stripped_ciphertext, b'{PASS}', bytes(hashed_pass, 'utf-8'))
    try:
        plaintext = decrypt(ciphertext)
    except DecryptKeyError as e:
        raise BadEncryptionPassword
    return plaintext

def file_encrypt(from_path, to_path, password=None, method=double_encrypt, **kwargs):
    from_file = open(from_path, 'r')
    lines = ''.join(from_file.readlines())
    from_file.close()
    if password:
        ciphertext = method(lines, password, **kwargs)
    else:
        ciphertext = method(lines, **kwargs)
    to_file = open(to_path, 'wb')
    to_file.write(ciphertext)
    to_file.close()

def file_decrypt(from_path, to_path, password=None, method=double_decrypt, **kwargs):
    from_file = open(from_path, 'rb')
    ciphertext = from_file.read()
    from_file.close()
    if password:
        plaintext = method(ciphertext, password, **kwargs)
    else:
        plaintext = method(ciphertext, **kwargs)
    to_file = open(to_path, 'w')
    to_file.write(plaintext)
    to_file.close()

