# Password Security System

A Python-based command-line password security project that demonstrates password strength analysis, secure password generation, encrypted password storage, and basic administrator management.

## Features

### User Panel
- Password strength checker based on length and character requirements
- Security suggestions for weak passwords
- Random password generator
- Password storage using Fernet symmetric encryption
- Retrieve a stored password by website name

### Admin Panel
- Admin registration and login
- Admin passwords stored as SHA-256 hashes
- View stored password entries
- Decrypt a stored password when required
- Delete stored password entries
- Count stored passwords

## Technologies

- Python
- `cryptography` / Fernet
- SHA-256 hashing
- File-based storage
- Command Line Interface (CLI)

## Project Structure

```text
password-security-system/
├── main.py
├── requirements.txt
├── .gitignore
├── README.md
├── admin/
│   ├── login.py
│   ├── register.py
│   └── logs.txt
└── user/
    ├── __init__.py
    ├── encryption.py
    ├── password_checker.py
    ├── password_generator.py
    ├── password_rules.py
    ├── password_store.py
    └── suggestions.py
```

## How to Run

1. Clone the repository.
2. Install the dependency:

```bash
pip install -r requirements.txt
```

3. Run the application from the project root:

```bash
python main.py
```

The encryption key is generated locally when the application first needs it. Local password data and the encryption key are intentionally excluded from Git using `.gitignore`.

## Security Notes

This is an educational cybersecurity project demonstrating basic password-security concepts. It is **not intended as a production password manager**. In particular, the admin authentication currently uses SHA-256 without a password-specific KDF/salt, and the encryption key is stored locally for the application.

Never commit real passwords, encryption keys, API keys, or other secrets to a public repository.

## Learning Outcomes

This project helped demonstrate:
- Password strength validation
- Password hashing concepts
- Symmetric encryption and decryption
- Secure random password generation concepts
- File-based authentication and storage
- Basic separation of user and administrator functionality
