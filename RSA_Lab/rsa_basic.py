'''
Noah Tugwell
CSCI 3740
20260917
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

# Step 4: Encrypt using the public key (n, e)
ciphertext = [pow(m, e, n) for m in message_ints]

# Step 5: Decrypt using the private key (n, d)
decrypted_ints = [pow(c, d, n) for c in ciphertext]

# Step 6: Convert the recovered integer back to text 
recovered_text = "".join(chr(m) for m in decrypted_ints)

 # Step 7: Print everything
print("Plaintext message:      ", plaintext)
print("Message as integer:     ", message_int)
print("Ciphertext (encrypted): ", ciphertext)
print("Decrypted integer:      ", decrypted_int)
print("Recovered plaintext:    ", recovered_text)
