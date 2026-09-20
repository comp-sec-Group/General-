'''
Joshua Vu
CSCI 3740
20260920
rsa_guess_attack.py
'''

# Step 1: RSA key setup
p = 61
q = 53

n = p * q
phi_n = (p - 1) * (q - 1)

e = 17
d = pow(e, -1, phi_n)

print("--- RSA Guessing Attack ---")
print("Public key  (n, e):", (n, e))

# Step 2: Create a small message space
candidates = ["YES", "NO"]

# Step 3: Choose the hidden challenge message
hidden_message = "NO"

# Step 4: Convert and encrypt the hidden message
hidden_ints = [ord(char) for char in hidden_message]
challenge_ciphertext = [pow(m, e, n) for m in hidden_ints]

print("\nChallenge ciphertext:", challenge_ciphertext)

# Step 5: Attacker encrypts each possible message
print("\n--- Attacker Guessing ---")

for guess in candidates:
    guess_ints = [ord(char) for char in guess]
    guess_ciphertext = [pow(m, e, n) for m in guess_ints]

    print("Candidate:", guess)
    print("Candidate ciphertext:", guess_ciphertext)

    # Step 6: Compare ciphertexts
    if guess_ciphertext == challenge_ciphertext:
        print("Match found!")
        print("Hidden message:", guess)
