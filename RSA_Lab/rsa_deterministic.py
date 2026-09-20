'''
Joshua Vu
CSCI 3740
20260920
rsa_deterministic.py
'''

# Step 1: RSA key setup
p = 61
q = 53

n = p * q
phi_n = (p - 1) * (q - 1)

e = 17
d = pow(e, -1, phi_n)

print("--- RSA Keys ---")
print("Public key  (n, e):", (n, e))
print("Private key (n, d):", (n, d))

# Take user input
filename = input("Enter the filename to read: ").strip()

# Step 2: Read the plaintext message from the file
with open(filename, "r") as f:
    plaintext = f.read().strip()

# Step 3: Convert the message into an integer
message_ints = [ord(char) for char in plaintext]

# Step 4: Encrypt the same message twice using the public key (n, e)
ciphertext1 = [pow(m, e, n) for m in message_ints]
ciphertext2 = [pow(m, e, n) for m in message_ints]

# Step 5: Compare both ciphertexts
same_ciphertext = ciphertext1 == ciphertext2

# Step 6: Print everything
print("Plaintext message:       ", plaintext)
print("Message as integer:      ", message_ints)
print("Ciphertext 1:            ", ciphertext1)
print("Ciphertext 2:            ", ciphertext2)
print("Ciphertexts identical:   ", same_ciphertext)
