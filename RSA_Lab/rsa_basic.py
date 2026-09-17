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
message_int = int("".join(str(ord(char)) for char in plaintext))

# Step 4: Encrypt using the public key (n, e)
ciphertext = pow(message_int, e, n)

# Step 5: Decrypt using the private key (n, d)
decrypted_int = pow(ciphertext, d, n)

# Step 6: Convert the recovered integer back to text 
decrypted_digits = str(decrypted_int)
if len(decrypted_digits) % 2 != 0:
	decrypted_digits = "0" + decrypted_digits

recovered_text = ""
for i in range(0, len(decrypted_digits), 2):
	code = int(decrypted_digits[i:i+2])
	recovered_text += chr(code)

 # Step 7: Print everything
print("Plaintext message:      ", plaintext)
print("Message as integer:     ", message_int)
print("Ciphertext (encrypted): ", ciphertext)
print("Decrypted integer:      ", decrypted_int)
print("Recovered plaintext:    ", recovered_text)
