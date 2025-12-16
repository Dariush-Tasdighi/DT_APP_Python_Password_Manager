# **************************************************
import os
import getpass
from rich import print


def main() -> None:
    """The main of program"""

    os.system(command="cls" if os.name == "nt" else "clear")

    password: str = getpass.getpass(prompt="Password: ")
    print(f"Your 'Password' is {password}")


if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print()

    except Exception as error:
        print(f"[-] {error}!")

    print()
# **************************************************


# **************************************************
# import os
# from rich import print
# from getpass import getpass


# def main() -> None:
#     """The main of program"""

#     os.system(command="cls" if os.name == "nt" else "clear")

#     password: str = getpass(prompt="Password: ")
#     print(f"Your 'Password' is {password}")


# if __name__ == "__main__":
#     try:
#         main()

#     except KeyboardInterrupt:
#         print()

#     except Exception as error:
#         print(f"[-] {error}!")

#     print()
# **************************************************
