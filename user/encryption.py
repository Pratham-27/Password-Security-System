from cryptography.fernet import Fernet
import os

key_file = "user/key.key"

def load_key():
    if not os.path.exists(key_file):
        key = Fernet.generate_key()
        with open(key_file, "wb") as file:
            file.write(key)

    with open(key_file, "rb") as file:
        return file.read()


key = load_key()
cipher = Fernet(key)


def encrypt_password(password):
    return cipher.encrypt(password.encode()).decode()


def decrypt_password(password):
    return cipher.decrypt(password.encode()).decode()