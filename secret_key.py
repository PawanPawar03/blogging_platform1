import os
 



# Generate a random byte string of 24 bytes
random_bytes = os.urandom(24)

# Convert the byte string to a hexadecimal string
secret_key = random_bytes.hex()

# print(secret_key)

print(f"Your secret key: {secret_key}")