import hashlib
#The hashlib module is a built-in Python module
#The hashlib modulethat provides a way to use various hashing algorithms to generate a fixed-length binary representation of a message or data.
#Hashing is a one-way function that takes an input (message or data) and generates a fixed-length output (hash) that is unique to that input.
#The hashlib module provides several hashing algorithms, including MD5, SHA-1, SHA-224, SHA-256, SHA-384, and SHA-512. 

for i in range(999,99999):
    password = str(i)
    if hashlib.md5(password.encode()).hexdigest() == "15825aee15eb335cc13f9b559f166ee8":
        print(f"Password found: {password}")
        break
    elif hashlib.sha1(password.encode()).hexdigest() == "15825aee15eb335cc13f9b559f166ee8":
        print(f"Password found: {password}")
        break