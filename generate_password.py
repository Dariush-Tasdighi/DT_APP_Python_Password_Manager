import os
import random
import string
import pyperclip


def generate_password(length: int = 24) -> str:
    """
    Generate a secure password with a specified length

    Args:
        length (int): Password length (minimum 4 characters)

    Returns:
        str: Generated password
    """

    if length < 4:
        message: str = "Password length must be at least 4 characters"
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


def main() -> None:
    """The main of program"""

    os.system(command="cls" if os.name == "nt" else "clear")

    # password: str = generate_password(length=3)
    # print(password)

    password: str = generate_password(length=12)
    print(password)
    pyperclip.copy(text=password)


if __name__ == "__main__":
    try:
        main()

    except Exception as error:
        print(f"[-] {error}!")

    print()
