'''
Joshua Vu
CSCI 3740
20260920
rsa_randomized_demo.py
'''

import secrets

# Step 1: RSA key setup
p = 61
q = 53

n = p * q
phi_n = (p - 1) * (q - 1)

e = 17
d = pow(e, -1, phi_n)

print("--- RSA Randomized Encryption Demo ---")
print("Public key  (n, e):", (n, e))

# Step 2: Original plaintext message
plaintext = "YES"

# Step 3: Generate two different random values
random1 = secrets.randbelow(1000)
random2 = secrets.randbelow(1000)

while random2 == random1:
    random2 = secrets.randbelow(1000)

# Step 4: Add randomness to the same original message
randomized_message1 = plaintext + str(random1)
randomized_message2 = plaintext + str(random2)

# Step 5: Convert both randomized messages into integers
message_ints1 = [ord(char) for char in randomized_message1]
message_ints2 = [ord(char) for char in randomized_message2]

# Step 6: Encrypt both randomized messages
ciphertext1 = [pow(m, e, n) for m in message_ints1]
ciphertext2 = [pow(m, e, n) for m in message_ints2]

# Step 7: Compare the ciphertexts
same_ciphertext = ciphertext1 == ciphertext2

# Step 8: Print everything
print("\nOriginal message:       ", plaintext)
print("Random value 1:         ", random1)
print("Random value 2:         ", random2)

print("\nRandomized message 1:   ", randomized_message1)
print("Randomized message 2:   ", randomized_message2)

print("\nCiphertext 1:            ", ciphertext1)
print("Ciphertext 2:            ", ciphertext2)

print("\nCiphertexts identical:   ", same_ciphertext)
