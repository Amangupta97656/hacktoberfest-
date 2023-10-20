import hashlib

def hash_string(input_string):
    # Create a new SHA-256 hash object
    sha256_hash = hashlib.sha256()

    # Update the hash object with the bytes of the input string
    sha256_hash.update(input_string.encode('utf-8'))

    # Get the hexadecimal representation of the hash
    hashed_string = sha256_hash.hexdigest()

    return hashed_string

# Input string to be hashed
input_string = "Hello, World!"

# Calculate the hash
hashed_result = hash_string(input_string)

print(f"Original String: {input_string}")
print(f"SHA-256 Hash: {hashed_result}")
