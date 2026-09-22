from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.PublicKey import RSA

key = RSA.generate(1024)
n, e, d = key.n, key.e, key.d

#Encrypt plaintext under a fresh AES-GCM session key, then wrap that key
#with the RSA public key. Returns (wrapped_key, nonce, tag, ciphertext)."""
def hybrid_encrypt(pt, n, e):
    sk = get_random_bytes(16)
    c = AES.new(sk, AES.MODE_GCM)
    ct, tag = c.encrypt_and_digest(pt)
    return pow(int.from_bytes(sk, 'big'), e, n), c.nonce, tag, ct
  
#Unwrap the session key with the RSA private exponent, then decrypt and
#verify the ciphertext. Raises ValueError if the GCM tag doesn't match.
def hybrid_decrypt(enc_sk, nonce, tag, ct, d, n):
    sk = pow(enc_sk, d, n).to_bytes(16, 'big')
    return AES.new(sk, AES.MODE_GCM, nonce=nonce).decrypt_and_verify(ct, tag)

msg = open("msg1.txt", "rb").read().strip()
enc_key, nonce, tag, ct = hybrid_encrypt(msg, n, e)

print(f"[*] Plaintext: {msg.decode()}")
print(f"[+] RSA-encrypted session key: {hex(enc_key)[:40]}...")
print(f"[+] Nonce: {nonce.hex()}")
print(f"[+] Ciphertext: {ct.hex()}")
print(f"[+] Recovered: {hybrid_decrypt(enc_key, nonce, tag, ct, d, n).decode()}")
