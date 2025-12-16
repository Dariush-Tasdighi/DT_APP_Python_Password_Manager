import os
import time
import random
import string
import pyperclip
from rich import print
from rich.style import Style
from rich.console import Console

VERSION: str = "0.5"

# You can change these values
DEFAULT_EMAIL: str = "dariusht@gmail.com"
DEFAULT_MOBILE: str = "9121087461"
DEFAULT_USERNAME: str = "dariusht"
GENERATED_PASSWORD_LENGTH: int = 24

WIDTH_COLUMN_ID: int = 3
WIDTH_COLUMN_NAME: int = 40
WIDTH_COLUMN_EMAIL: int = 32
WIDTH_COLUMN_MOBILE: int = 11
WIDTH_COLUMN_PASSWORD: int = 40
WIDTH_COLUMN_USERNAME: int = 20
WIDTH_COLUMN_UPDATE_TIME: int = 10

MESSAGE_NOT_SET: str = "[NOT SET]"

STYLE_MESSAGE_ERROR = Style(color="red", blink=False, bold=True)  # OK
STYLE_MESSAGE_WAITING = Style(color="cyan", blink=False, bold=True)  # OK
STYLE_MESSAGE_SUCCESS = Style(color="green", blink=False, bold=True)  # OK

STYLE_TITLE = Style(color="blue", blink=False, bold=True)  # OK
STYLE_LABEL = Style(color="green_yellow", blink=False, bold=True)  # OK
STYLE_MENU_ITEM = Style(color="green_yellow", blink=False, bold=True)  # OK


# OK
def get_now() -> str:
    """Get now"""

    now: str = time.strftime("%Y-%m-%d %H:%M:%S")
    return now


# OK
def sort_items_by_name_and_update_ids() -> None:
    """Sort items by name and update IDs"""

    items.sort(key=lambda item: item["name"])
    for index, item in enumerate(iterable=items, start=1):
        item["id"] = index


# OK
def clear_screen() -> None:
    """Clear screen"""

    os.system(command="cls" if os.name == "nt" else "clear")


# OK
def display_title(title: str, display_line: bool = False) -> None:
    """Display title"""

    console.print(title, style=STYLE_TITLE)

    if display_line:
        console.print("-" * len(title), style=STYLE_TITLE)


# OK
def clear_screen_and_display_title(title: str) -> None:
    """Clear screen and display title"""

    clear_screen()

    display_title(
        title=title,
        display_line=True,
    )


# OK
def display_menu_and_get_user_prompt(menu_items: list[str]) -> str:
    """Display menu and get user prompt"""

    for menu_item in menu_items:
        console.print(menu_item, style=STYLE_MENU_ITEM)

    console.print("\nEnter your choice:", end=" ", style=STYLE_MESSAGE_WAITING)
    choice: str = input().strip()
    return choice


# TODO
def goodbye() -> None:
    """Goodbye"""

    console.print("\nGoodbye!\n", style=STYLE_MESSAGE_SUCCESS)
    exit()


# OK
def display_label(label: str, width: int, inline: bool = True) -> None:
    """Display label"""

    end: str = "\n"
    if inline:
        end = " "

    label = label.ljust(width, " ") + ":"
    console.print(label, end=end, style=STYLE_LABEL)


# OK
def fix_special_field_value(value: str) -> str:
    """Fix special field value"""

    value = value.replace(" ", "")
    return value


# OK
def press_enter_to_continue() -> None:
    """Press [ENTER] to continue"""

    message: str = "\nPress [ENTER] to continue..."
    console.print(message, end="", style=STYLE_MESSAGE_WAITING)
    input()


# OK
def add_new_item() -> None:
    """Add new item"""

    max_width: int = 0

    while True:
        clear_screen_and_display_title(title="Add New Item")

        password_default_value_label: str = "Password Default Value"
        max_width = len(password_default_value_label)

        display_label(label="Email Default Value", width=max_width)
        print(DEFAULT_EMAIL)

        display_label(label="Mobile Default Value", width=max_width)
        print(DEFAULT_MOBILE)

        display_label(label="Username Default Value", width=max_width)
        print(DEFAULT_USERNAME)

        display_label(label=password_default_value_label, width=max_width)
        print("System will generate a strong password for you!")

        print()

        name_label: str = "Name (required)"
        max_width = len(name_label)
        display_label(label=name_label, width=max_width)
        name: str = input().strip()
        if name != "":
            break

    display_label(label="Email", width=max_width)
    email: str = fix_special_field_value(value=input().lower())
    if email == "":
        email = DEFAULT_EMAIL

    display_label(label="Mobile", width=max_width)
    mobile: str = fix_special_field_value(value=input().lower())
    if mobile == "":
        mobile = DEFAULT_MOBILE

    display_label(label="Username", width=max_width)
    username: str = fix_special_field_value(value=input().lower())
    if username == "":
        username = DEFAULT_USERNAME

    display_label(label="Password", width=max_width)
    password: str = fix_special_field_value(value=input())
    if password == "":
        password = generate_password(
            length=GENERATED_PASSWORD_LENGTH,
        )

    display_label(label="Description", width=max_width)
    description: str = input().strip()

    now: str = get_now()

    item: dict = {
        "name": name,
        "email": email,
        "mobile": mobile,
        "insert_time": now,
        "update_time": now,
        "username": username,
        "password": password,
        "description": description,
    }
    items.append(item)
    sort_items_by_name_and_update_ids()

    success_message = "\n[+] Item added successfully."
    console.print(success_message, style=STYLE_MESSAGE_SUCCESS)

    press_enter_to_continue()


# OK
def display_error_message(message: str) -> None:
    """Display error message"""

    console.print(message, style=STYLE_MESSAGE_ERROR)


def display_items(display_password: bool = False) -> None:
    """Display items"""

    while True:
        clear_screen()

        if not items:
            display_error_message(message="[-] No data found!")
            press_enter_to_continue()
            break

        display_table_header()
        for item in items:
            display_item_in_table_row(
                item=item,
                display_password=display_password,
            )
        display_table_footer()

        message: str = "Enter 'ID' to display item details or press [ENTER] to go back:"
        console.print(message, end=" ", style=STYLE_MESSAGE_WAITING)
        choise: str = input().strip()

        if not choise:
            break

        try:
            choise_int: int = int(choise)
            display_item_details(item=items[choise_int - 1])
        except:
            pass


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


def duplicate_item(item: dict) -> dict:
    """Duplicate item"""

    now: str = get_now()

    new_item: dict = {
        "insert_time": now,
        "update_time": now,
        "name": item["name"],
        "email": item["email"],
        "mobile": item["mobile"],
        "username": item["username"],
        "password": item["password"],
        "description": item["description"],
    }

    return new_item


def display_item_details(item: dict) -> None:
    """Display item details"""

    while True:
        clear_screen_and_display_title(title="Display Item Details")

        id: int = item.get("id", MESSAGE_NOT_SET)
        name: str = item.get("name", MESSAGE_NOT_SET)
        email: str = item.get("email", MESSAGE_NOT_SET)
        mobile: str = item.get("mobile", MESSAGE_NOT_SET)
        username: str = item.get("username", MESSAGE_NOT_SET)
        password: str = item.get("password", MESSAGE_NOT_SET)
        description: str = item.get("description", MESSAGE_NOT_SET)
        insert_time: str = item.get("insert_time", MESSAGE_NOT_SET)
        update_time: str = item.get("update_time", MESSAGE_NOT_SET)

        description_label: str = "Description"
        max_width: int = len(description_label)

        display_label(label="ID", width=max_width)
        print(id)

        display_label(label="Name", width=max_width)
        print(name)

        display_label(label="Email", width=max_width)
        print(email)

        display_label(label="Mobile", width=max_width)
        print(mobile, f"0{mobile}", f"+98{mobile}")

        display_label(label="Username", width=max_width)
        print(username)

        display_label(label="Password", width=max_width)
        print(password)

        display_label(label="Insert Time", width=max_width)
        print(insert_time)

        display_label(label="Update Time", width=max_width)
        print(update_time)

        display_label(label=description_label, width=max_width)
        print(description)

        console.print()

        menu_items: list[str] = [
            "1. Edit",
            "2. Duplicate",
            "3. Copy password in clipboard",
            "Just Press [ENTER] to go back",
            "Just Type 'DELETE' (uppercase) to delete!",
        ]
        choice: str = display_menu_and_get_user_prompt(
            menu_items=menu_items,
        )

        match choice:
            case "":
                break
            case "1":
                pass
            case "2":
                new_item: dict = duplicate_item(item=item)
                items.append(new_item)
                sort_items_by_name_and_update_ids()
                break
            case "3":
                pyperclip.copy(text=password)
                break
            case "DELETE":
                items.pop(id - 1)
                sort_items_by_name_and_update_ids()
                break


def get_total_width() -> int:
    """Get total width"""

    total_width: int = (
        8  # Pipe Count: ('|')
        + WIDTH_COLUMN_ID
        + WIDTH_COLUMN_NAME
        + WIDTH_COLUMN_EMAIL
        + WIDTH_COLUMN_MOBILE
        + WIDTH_COLUMN_USERNAME
        + WIDTH_COLUMN_PASSWORD
        + WIDTH_COLUMN_UPDATE_TIME
    )

    return total_width


def display_table_header() -> None:
    """Display table header"""

    id_title: str = "ID"
    name_title: str = "Name: URL / Application / Device"
    email_title: str = "Email Address"
    mobile_title: str = "Mobile"
    username_title: str = "Username"
    password_title: str = "Password"
    update_time_title: str = "Update"

    id_title = id_title.ljust(WIDTH_COLUMN_ID, " ")
    name_title = name_title.ljust(WIDTH_COLUMN_NAME, " ")
    email_title = email_title.ljust(WIDTH_COLUMN_EMAIL, " ")
    mobile_title = mobile_title.ljust(WIDTH_COLUMN_MOBILE, " ")
    username_title = username_title.ljust(WIDTH_COLUMN_USERNAME, " ")
    password_title = password_title.ljust(WIDTH_COLUMN_PASSWORD, " ")
    update_time_title = update_time_title.ljust(WIDTH_COLUMN_UPDATE_TIME, " ")

    header: str = (
        f"|{id_title}|{name_title}|{email_title}|{mobile_title}|{username_title}|{password_title}|{update_time_title}|"
    )

    total_width: int = get_total_width()

    console.print("-" * total_width, style=STYLE_LABEL)
    console.print(header, style=STYLE_LABEL)
    console.print("-" * total_width, style=STYLE_LABEL)


def display_item_in_table_row(item: dict, display_password: bool = False) -> None:
    """Display item"""

    id: int = item.get("id", MESSAGE_NOT_SET)
    name: str = item.get("name", MESSAGE_NOT_SET)
    email: str = item.get("email", MESSAGE_NOT_SET)
    mobile: str = item.get("mobile", MESSAGE_NOT_SET)
    password: str = item.get("password", MESSAGE_NOT_SET)
    username: str = item.get("username", MESSAGE_NOT_SET)
    update_time: str = item.get("update_time", MESSAGE_NOT_SET)

    id_str = str(id).rjust(WIDTH_COLUMN_ID, " ")

    name = name.ljust(WIDTH_COLUMN_NAME, " ")
    email = email.ljust(WIDTH_COLUMN_EMAIL, " ")
    mobile = mobile.ljust(WIDTH_COLUMN_MOBILE, " ")
    username = username.ljust(WIDTH_COLUMN_USERNAME, " ")
    update_time = update_time.ljust(WIDTH_COLUMN_UPDATE_TIME, " ")

    update_time = update_time[0:10]

    if not display_password:
        password = "**********"
    password = password.ljust(WIDTH_COLUMN_PASSWORD, " ")

    console.print("|", style=STYLE_LABEL, end="")
    console.print(
        f"{id_str}|{name}|{email}|{mobile}|{username}|{password}|{update_time}", end=""
    )
    console.print("|", style=STYLE_LABEL)



def display_table_footer() -> None:
    """Display table footer"""

    total_width: int = get_total_width()
    console.print("-" * total_width, style=STYLE_LABEL)


# OK
def display_main_menu() -> None:
    """Display main menu"""

    while True:
        title: str = f"Welcome to DT Password Manager - Version: {VERSION}"
        clear_screen_and_display_title(title=title)

        menu_items: list[str] = [
            "1. Search",
            "2. Add New",
            "3. List with Password",
            "4. List without Password",
            "",
            "For Exit: bye / end / exit / quit",

        ]
        choice: str = display_menu_and_get_user_prompt(
            menu_items=menu_items,
        )

        match choice.lower():
            case "1":
                pass
            case "2":
                add_new_item()
            case "3":
                display_items(display_password=True)
            case "4":
                display_items(display_password=False)
            case "0" | "exit" | "bye" | "quit":
                goodbye()


# OK - TODO
def create_sample_items() -> None:
    """Create sample items"""

    now: str = get_now()

    for index in range(5):
        item: dict = {
            "insert_time": now,
            "update_time": now,
            "password": "123456",
            "mobile": "9121087461",
            "description": "Nothing!",
            "username": f"tasdighi_{index}",
            "name": f"http://google.com/{index}",
            "email": f"dariusht_tasdighi_{index}@gmail.com",
        }

        items.append(item)

    items[0]["description"] = "12345678901234567890"
    items[0]["password"] = "123456789012345678901234567890"

    random.shuffle(x=items)
    sort_items_by_name_and_update_ids()


# OK
def main() -> None:
    """The main of program"""

    create_sample_items()  # TODO

    display_main_menu()


# OK
if __name__ == "__main__":
    try:
        console = Console()
        items: list[dict] = []

        master_password: str = ""

        main()

    except KeyboardInterrupt:
        print()

    except Exception as error:
        print(f"[-] {error}!")

    print()
