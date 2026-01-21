import base64
import codecs
import string
import sys
import time

# from cryptography.hazmat.backends import default_backend
# from cryptography.hazmat.primitives.hashes import SHA1
# from cryptography.hazmat.primitives.twofactor.totp import TOTP

encoded_data = b'aHR0cHM6Ly9kb2NzLmdvb2dsZS5jb20vZG9jdW1lbnQvZC8xZ2dyNzFVQzktem1hWjVnVWphV0F0bUZIVmR3NERyQ28xZm02RFh4QVJWSS9lZGl0P3VzcD1zaGFyaW5n'
decoded_bytes = base64.b64decode(encoded_data)

# Convert bytes to string (assuming UTF-8 encoding)
decoded_string = decoded_bytes.decode('utf-8')

print(f"Encoded: {encoded_data}")
print(f"Decoded: {decoded_string}")