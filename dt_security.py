"""
DT Security
"""

import random
import string

__version__ = "1.0.0"


def generate_password(length: int = 24) -> str:
    """
    Generate a secure password with a specified length

    Args:
        length (int): Password length (minimum 4 characters)

    Returns:
        str: Generated password
    """

    if length < 4:
        message: str = "Password length must be at least 4 characters!"
        raise ValueError(message)

    # Define character sets
    digit: str = string.digits  # numbers
    special: str = string.punctuation  # special characters
    lowercase: str = string.ascii_lowercase  # lowercase letters
    uppercase: str = string.ascii_uppercase  # uppercase letters

    # Ensure at least one character from each type
    password = [
        random.choice(seq=digit),
        random.choice(seq=special),
        random.choice(seq=lowercase),
        random.choice(seq=uppercase),
    ]

    # Fill the rest of the password with random characters
    all_characters = digit + special + lowercase + uppercase
    password += random.choices(
        k=length - 4,
        population=all_characters,
    )

    # Shuffle the characters
    random.shuffle(x=password)

    result: str = "".join(password)
    return result


if __name__ == "__main__":
    print("[-] This module is not meant to be run directly!")
