"""
Quantum Resistant Encryption
"""

import os
from rich import print
from getpass import getpass
from dt_cryptography import encrypt_plain_text
from dt_cryptography import decrypt_encrypted_data
from dt_cryptography import validate_password_strength


def main() -> None:
    """The main of program"""

    os.system(command="cls" if os.name == "nt" else "clear")

    print("=" * 50)
    print("Quantum Resistant Encryption (AES-256-GCM)")
    print("-" * 50)
    print("Security Note:")
    print("- AES-256 provides ~128-bit quantum resistance")
    print("- Grover's algorithm reduces effective strength by half")
    print("- Still secure against current and near-future quantum computers")
    print("=" * 50)

    # Sample text to encrypt
    plain_text: str = """
    This is a highly confidential message that needs protection against quantum computer attacks. AES-256 provides sufficient security for the next 20-30 years.
    """
    plain_text = plain_text.strip()

    print()
    print("=" * 50)
    print("'Plain Text':")
    print(plain_text)
    print("=" * 50)
    print()

    while True:
        prompt = "Enter password for encryption (minimum 16 characters): "
        password: str = getpass(prompt=prompt)
        is_valid, message = validate_password_strength(password=password)
        if is_valid:
            print(f"✓ {message}")
            break
        else:
            print(f"✗ {message}")
            print()

    # Encrypt the text
    print()
    print("=" * 50)
    print("Encrypting...")
    print("=" * 50)
    encrypted_data: dict = encrypt_plain_text(
        password=password,
        plain_text=plain_text,
    )

    print()
    print("=" * 50)
    print("Encrypted Data:")
    print("-" * 50)
    print(f"'Nonce'     : {encrypted_data['nonce'][:32]}...")
    print(f"'Salt'      : {encrypted_data['salt'][:32]}...")
    print(f"'Auth Tag'  : {encrypted_data['tag']}")
    print(f"'Ciphertext': {encrypted_data['ciphertext'][:50]}...")
    print("=" * 50)

    print()
    prompt: str = "Enter password for decryption: "
    password_new: str = getpass(prompt=prompt)

    print()
    print("=" * 50)
    print("Decrypting...")
    print("=" * 50)

    is_decrypted: bool
    plain_text_new: str

    is_decrypted, plain_text_new = decrypt_encrypted_data(
        password=password_new,
        encrypted_data=encrypted_data,
    )

    print()
    print("=" * 50)
    if is_decrypted:
        print("✓ Decryption Successful!")
        print("-" * 50)
        print("'Decrypted Text':")
        print(plain_text_new)

        if plain_text == plain_text_new:
            print("-" * 50)
            print("✓ Data integrity verified and No tampering detected.")
        else:
            print("-" * 50)
            print("✗ Decryption Failed!")
    else:
        print("✗ Decryption Failed!")

    print("=" * 50)


if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print()

    except Exception as error:
        print(f"\n[-] {error}!")

    print()
