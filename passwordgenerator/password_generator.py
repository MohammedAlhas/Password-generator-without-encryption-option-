import random
import string
import hashlib
import hmac
import os
import base64
import bcrypt

# Random Password Generator
def random_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(length))

# SHA-256 Password Hashing
def sha256_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# HMAC Password Hashing
def hmac_password(password, key=None):
    if key is None:
        key = os.urandom(16)  # Generate a random key
    hashed_password = hmac.new(key, password.encode(), hashlib.sha256).digest()
    return base64.b64encode(key + hashed_password).decode('utf-8')

# bcrypt Password Hashing
def bcrypt_password(password):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(), salt).decode()

# Main function to run all algorithms
def main():
    print("Password Generator Tool")
    base_password = input("Enter the base password: ")
    random_length = int(input("Enter the length for the random password: "))

    # Generate Random Password
    print("\nGenerated Passwords:")
    print(f"Random Password: {random_password(random_length)}")

    # Generate SHA-256 Hashed Password
    print(f"SHA-256 Hashed Password: {sha256_password(base_password)}")

    # Generate HMAC Hashed Password
    print(f"HMAC Hashed Password: {hmac_password(base_password)}")

    # Generate bcrypt Hashed Password
    print(f"bcrypt Hashed Password: {bcrypt_password(base_password)}")

if __name__ == "__main__":
    main()
