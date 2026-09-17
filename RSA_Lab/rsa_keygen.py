"""
Noah Tugwell
CSCI 3740
20260917
rsa_keygen.py
This is a Generation of RSA key
"""

# Step 1: Pick two prime nums
p = 61
q = 53

# Step 2: Cumpute n = p * q
n = p * q

#Step 3: phi(n)
phi_n = (p-1) * (q -1)

#Step 4: Choose public exponent e
e = 17

#Step 5: Comute exponent d
d = pow(e, -1, phi_n)

#Step 6: Print Private and public key
print("Public key ", (n, e))
print("\nPrivate key ", (n,d))

#Step 7: Verify 
check = (e * d) % phi_n
print("\nCheck ", check)
print("\nShould be 1 ", check == 1) 
