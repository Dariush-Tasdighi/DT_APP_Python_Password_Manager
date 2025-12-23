import os
import base64
import getpass

from cryptography.hazmat.backends import default_backend

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import modes
from cryptography.hazmat.primitives.ciphers import Cipher
from cryptography.hazmat.primitives.ciphers import algorithms
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2


def derive_key_from_password(password: str, salt: bytes) -> bytes:
    """
    Derive a 256-bit encryption key from password using PBKDF2

    Args:
        password (str): User's password
        salt (bytes): 16-byte random salt for key derivation

    Returns:
        bytes: 32-byte (256-bit) key for AES-256
    """

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,  # 256 bits for AES-256
        salt=salt,
        iterations=600_000,  # OWASP recommendation (2023+)
        backend=default_backend(),
    )

    return kdf.derive(password.encode("utf-8"))


def encrypt_text(plaintext: str, password: str) -> dict:
    """
    Encrypt text using AES-256-GCM (Quantum-resistant symmetric encryption)

    AES-256 provides approximately 128-bit security against quantum computers
    (Grover's algorithm reduces effective key length by half)

    Args:
        plaintext (str): Text to encrypt
        password (str): User's password (minimum 16 characters recommended)

    Returns:
        dict: Contains salt, nonce, ciphertext, and authentication tag
    """

    # Generate random salt (16 bytes)
    salt = os.urandom(16)

    # Derive 256-bit key from password
    key = derive_key_from_password(password, salt)

    # Generate random nonce (12 bytes for GCM)
    nonce = os.urandom(12)

    # Create AES-256-GCM cipher
    cipher = Cipher(algorithms.AES(key), modes.GCM(nonce), backend=default_backend())
    encryptor = cipher.encryptor()

    # Encrypt the plaintext
    ciphertext = encryptor.update(plaintext.encode("utf-8")) + encryptor.finalize()

    # Get authentication tag (prevents tampering)
    tag = encryptor.tag

    # Return all components needed for decryption
    return {
        "salt": base64.b64encode(salt).decode("utf-8"),
        "nonce": base64.b64encode(nonce).decode("utf-8"),
        "ciphertext": base64.b64encode(ciphertext).decode("utf-8"),
        "tag": base64.b64encode(tag).decode("utf-8"),
    }


def decrypt_text(encrypted_data: dict, password: str) -> str:
    """
    Decrypt text encrypted with AES-256-GCM

    Args:
        encrypted_data (dict): Dictionary containing salt, nonce, ciphertext, tag
        password (str): User's password (must match encryption password)

    Returns:
        str: Decrypted plaintext

    Raises:
        Exception: If password is wrong, data is corrupted, or tampered
    """

    try:
        # Decode Base64 components
        salt = base64.b64decode(encrypted_data["salt"])
        nonce = base64.b64decode(encrypted_data["nonce"])
        ciphertext = base64.b64decode(encrypted_data["ciphertext"])
        tag = base64.b64decode(encrypted_data["tag"])

        # Derive the same key from password and salt
        key = derive_key_from_password(password, salt)

        # Create AES-256-GCM cipher with authentication tag
        cipher = Cipher(
            algorithms.AES(key), modes.GCM(nonce, tag), backend=default_backend()
        )
        decryptor = cipher.decryptor()

        # Decrypt and verify authentication
        plaintext = decryptor.update(ciphertext) + decryptor.finalize()

        return plaintext.decode("utf-8")

    except Exception as e:
        raise Exception(
            f"Decryption failed! Wrong password or data corrupted/tampered. Error: {str(e)}"
        )


def validate_password_strength(password: str) -> tuple:
    """
    Check if password is strong enough for quantum-resistant encryption

    Args:
        password (str): Password to validate

    Returns:
        tuple: (is_valid: bool, message: str)
    """
    if len(password) < 16:
        return False, "Password must be at least 16 characters for quantum resistance"

    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)

    if not (has_upper and has_lower and has_digit and has_special):
        return (
            False,
            "Password must contain uppercase, lowercase, digits, and special characters",
        )

    return True, "Password is strong"


# Example usage
if __name__ == "__main__":
    print("=" * 60)
    print("QUANTUM-RESISTANT ENCRYPTION (AES-256-GCM)")
    print("=" * 60)
    print("\nSecurity Note:")
    print("- AES-256 provides ~128-bit quantum resistance")
    print("- Grover's algorithm reduces effective strength by half")
    print("- Still secure against current and near-future quantum computers")
    print("=" * 60 + "\n")

    # Sample text to encrypt
    original_text = """This is a highly confidential message that needs 
protection against quantum computer attacks. AES-256 provides 
sufficient security for the next 20-30 years."""

    print("Original Text:")
    print(f'"{original_text}"')
    print("\n" + "=" * 60 + "\n")

    # Get password for encryption
    while True:
        password = getpass.getpass("Enter password for encryption (min 16 chars): ")
        is_valid, message = validate_password_strength(password)
        if is_valid:
            print(f"✓ {message}\n")
            break
        else:
            print(f"✗ {message}\n")

    # Encrypt the text
    print("Encrypting...")
    encrypted_data = encrypt_text(original_text, password)

    print("\nEncrypted Data:")
    print(f"Salt: {encrypted_data['salt'][:32]}...")
    print(f"Nonce: {encrypted_data['nonce'][:32]}...")
    print(f"Ciphertext: {encrypted_data['ciphertext'][:50]}...")
    print(f"Auth Tag: {encrypted_data['tag']}")
    print("\n" + "=" * 60 + "\n")

    # Get password for decryption
    password_decrypt = getpass.getpass("Enter password for decryption: ")

    # Decrypt the text
    print("\nDecrypting...")
    try:
        decrypted_text = decrypt_text(encrypted_data, password_decrypt)
        print("\n✓ Decryption Successful!")
        print("\nDecrypted Text:")
        print(f'"{decrypted_text}"')

        # Verify integrity
        if decrypted_text == original_text:
            print("\n✓ Data integrity verified - No tampering detected")

    except Exception as e:
        print(f"\n✗ Error: {e}")
