# Password Generator Tool

This repository contains a password generator tool that offers various password generation and hashing techniques. The tool includes functionalities for generating random passwords and hashing passwords using different algorithms, such as SHA-256, HMAC, and bcrypt.

## Scripts

1. **`bcrypt_password.py`**
   - **Description**: This script hashes a password using the bcrypt hashing algorithm.
   - **Function**: 
     ```python
     def bcrypt_password(password):
         salt = bcrypt.gensalt()
         return bcrypt.hashpw(password.encode(), salt).decode()
     ```
   - **Usage**: Run the script, input the password, and it will return the bcrypt hashed password.

2. **`hmac_password.py`**
   - **Description**: This script hashes a password using HMAC with SHA-256.
   - **Function**: 
     ```python
     def hmac_password(password, key=None):
         if key is None:
             key = os.urandom(16)  # Generate a random key
         hashed_password = hmac.new(key, password.encode(), hashlib.sha256).digest()
         return base64.b64encode(key + hashed_password).decode('utf-8')
     ```
   - **Usage**: Run the script, input the password, and it will return the HMAC hashed password.

3. **`random_password.py`**
   - **Description**: This script generates a random password of a specified length.
   - **Function**: 
     ```python
     def random_password(length=12):
         characters = string.ascii_letters + string.digits + string.punctuation
         return ''.join(random.choice(characters) for i in range(length))
     ```
   - **Usage**: Run the script, input the desired length, and it will return a random password.

4. **`sha256_password.py`**
   - **Description**: This script hashes a password using the SHA-256 algorithm.
   - **Function**: 
     ```python
     def sha256_password(password):
         return hashlib.sha256(password.encode()).hexdigest()
     ```
   - **Usage**: Run the script, input the password, and it will return the SHA-256 hashed password.

5. **`password_generator.py`**
   - **Description**: This is the main script that ties together all the functionalities of the above scripts.
   - **Function**: It generates a random password, hashes a base password using SHA-256, HMAC, and bcrypt.
   - **Usage**: Run the script, input a base password and the desired length for the random password, and it will display the results.

## Setup Guide

### Prerequisites

Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

# Commands for Password Generator Tool

## Clone the repository
git clone https://github.com/MohammedAlhas/automated-pt-framework.git
cd automated-pt-framework

## Install the required packages
pip install bcrypt

## Run any individual script
python <script_name>.py

## Run the main password generator tool
python password_generator.py
