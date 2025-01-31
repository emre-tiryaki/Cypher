# Encryption

This project implements a very simple encryption and decryption mechanism using a shuffled key based on ASCII characters.

## Files

-cypher.py : The main script that handles encryption and decryption.

## Usage

1. Run the countdown.py script.
2. Enter the text you want to encrypt when prompted.
3. The script will display the encrypted text.
4. Enter the encrypted text to decrypt it.
5. The script will display the decrypted text.

## Example

```sh
python countdown.py
The text you want to encrypt: Hello, World!
Encrypted text: <encrypted_text>
The text you want to decypher: <encrypted_text>
Decrypted text: Hello, World!
```

## Functions

- encrypt(plain_text: str) -> str: Encrypts the given plain text using the shuffled key.
- decrypt(encrypted_text: str) -> str: Decrypts the given encrypted text using the shuffled key.

## Notes

- The encryption key is generated randomly each time the script is run, so the same plain text will produce different encrypted texts in different runs.
- The script uses all ASCII letters, digits, punctuation, and space for encryption.
