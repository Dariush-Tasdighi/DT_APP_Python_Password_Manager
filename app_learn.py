import os
import time
import random
import pyperclip
from rich import print
from rich.console import Console
from dt_cryptography import generate_password

# import app_constants
# import app_constants as constants
from app_constants import *

__version__ = "0.6"


def get_now() -> str:
    """Get now"""

    now: str = time.strftime("%Y-%m-%d %H:%M:%S")
    return now


def sort_items_by_name_and_update_ids() -> None:
    """Sort items by name and update IDs"""

    items.sort(key=lambda item: item[KEY_NAME_NAME])
    for index, item in enumerate(iterable=items, start=1):
        item[KEY_NAME_ID] = index


def clear_screen() -> None:
    """Clear screen"""

    os.system(command="cls" if os.name == "nt" else "clear")


def display(title: str, display_line: bool = False) -> None:
    """Display title"""

    console.print(title, style=STYLE_COLUMN_HEADER)

    if display_line:
        console.print("-" * len(title), style=STYLE_COLUMN_HEADER)


def clear_screen_and_display(title: str) -> None:
    """Clear screen and display title"""

    clear_screen()

    display(
        title=title,
        display_line=True,
    )


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


def display_label(label: str, width: int, inline: bool = True) -> None:
    """Display label"""

    end: str = "\n"
    if inline:
        end = " "

    label = label.ljust(width, " ") + ":"
    console.print(label, end=end, style=STYLE_LABEL)


def fix_special_field_value(value: str) -> str:
    """Fix special field value"""

    value = value.replace(" ", "")
    return value


def press_enter_to_continue() -> None:
    """Press [ENTER] to continue"""

    message: str = "\nPress [ENTER] to continue..."
    console.print(message, end="", style=STYLE_MESSAGE_WAITING)
    input()


def add_new_item() -> None:
    """Add new item"""

    default_password_label: str = f"Default {LABEL_PASSWORD}"
    max_width: int = len(default_password_label)

    while True:
        clear_screen_and_display(title="Add New Item")

        display_label(label=f"Default {LABEL_EMAIL}", width=max_width)
        print(DEFAULT_EMAIL)

        display_label(label=f"Default {LABEL_MOBILE}", width=max_width)
        print(DEFAULT_MOBILE)

        display_label(label=f"Default {LABEL_USERNAME}", width=max_width)
        print(DEFAULT_USERNAME)

        display_label(label=default_password_label, width=max_width)
        print("System will generate a strong password!")

        print()

        label_name: str = f"{LABEL_NAME} (required)"
        display_label(label=label_name, width=max_width)
        name: str = input().strip()
        if name != "":
            break

    display_label(label=LABEL_EMAIL, width=max_width)
    email: str = fix_special_field_value(value=input().lower())
    if email == "":
        email = DEFAULT_EMAIL

    display_label(label=LABEL_MOBILE, width=max_width)
    mobile: str = fix_special_field_value(value=input().lower())
    if mobile == "":
        mobile = DEFAULT_MOBILE

    display_label(label=LABEL_USERNAME, width=max_width)
    username: str = fix_special_field_value(value=input().lower())
    if username == "":
        username = DEFAULT_USERNAME

    display_label(label=LABEL_PASSWORD, width=max_width)
    password: str = fix_special_field_value(value=input())
    if password == "":
        password = generate_password(
            length=GENERATED_PASSWORD_LENGTH,
        )

    display_label(label=LABEL_DESCRIPTION, width=max_width)
    description: str = input().strip()

    now: str = get_now()

    item: dict = {
        KEY_NAME_NAME: name,
        KEY_NAME_EMAIL: email,
        KEY_NAME_MOBILE: mobile,
        KEY_NAME_PASSWORD: password,
        KEY_NAME_USERNAME: username,
        KEY_NAME_DESCRIPTION: description,
        #
        KEY_NAME_INSERT_TIME: now,
        KEY_NAME_UPDATE_TIME: now,
    }

    items.append(item)

    sort_items_by_name_and_update_ids()

    success_message = "\n[+] Item added successfully."
    console.print(success_message, style=STYLE_MESSAGE_SUCCESS)

    press_enter_to_continue()


def edit_item(item: dict) -> None:
    """Edit item"""

    clear_screen_and_display(title="Edit Item")

    label_password: str = f"{LABEL_PASSWORD} (NEW)"
    max_width: int = len(label_password)

    display_label(label=LABEL_ID, width=max_width)
    print(item.get(KEY_NAME_ID, MESSAGE_NOT_SET))

    display_label(label=LABEL_NAME, width=max_width)
    print(item.get(KEY_NAME_NAME, MESSAGE_NOT_SET))

    display_label(label=LABEL_EMAIL, width=max_width)
    print(item.get(KEY_NAME_NAME, MESSAGE_NOT_SET))

    display_label(label=LABEL_MOBILE, width=max_width)
    print(item.get(KEY_NAME_MOBILE, MESSAGE_NOT_SET))

    display_label(label=LABEL_USERNAME, width=max_width)
    print(item.get(KEY_NAME_USERNAME, MESSAGE_NOT_SET))

    display_label(label=LABEL_PASSWORD, width=max_width)
    print(item.get(KEY_NAME_PASSWORD, MESSAGE_NOT_SET))

    display_label(label=LABEL_DESCRIPTION, width=max_width)
    print(item.get(KEY_NAME_DESCRIPTION, MESSAGE_NOT_SET))

    print()

    updated: bool = False

    display_label(label=LABEL_NAME, width=max_width)
    name: str = input().strip()
    if name == "":
        name = item[KEY_NAME_NAME]
    else:
        updated = True

    display_label(label=LABEL_EMAIL, width=max_width)
    email: str = fix_special_field_value(value=input().lower())
    if email == "":
        email = item[KEY_NAME_EMAIL]
    else:
        updated = True

    display_label(label=LABEL_MOBILE, width=max_width)
    mobile: str = fix_special_field_value(value=input().lower())
    if mobile == "":
        mobile = item[KEY_NAME_MOBILE]
    else:
        updated = True

    display_label(label=LABEL_USERNAME, width=max_width)
    username: str = fix_special_field_value(value=input().lower())
    if username == "":
        username = item[KEY_NAME_USERNAME]
    else:
        updated = True

    display_label(label=label_password, width=max_width)
    password: str = fix_special_field_value(value=input())
    if password == "":
        password = item[KEY_NAME_PASSWORD]
    elif password.upper() == "NEW":
        updated = True
        password = generate_password(
            length=GENERATED_PASSWORD_LENGTH,
        )
    else:
        updated = True

    display_label(label=LABEL_DESCRIPTION, width=max_width)
    description: str = input().strip()
    if description == "":
        description = item[KEY_NAME_DESCRIPTION]
    else:
        updated = True

    if updated:
        now: str = get_now()

        item.update(
            {
                KEY_NAME_NAME: name,
                KEY_NAME_EMAIL: email,
                KEY_NAME_MOBILE: mobile,
                KEY_NAME_PASSWORD: password,
                KEY_NAME_USERNAME: username,
                KEY_NAME_DESCRIPTION: description,
                #
                KEY_NAME_UPDATE_TIME: now,
            }
        )

        sort_items_by_name_and_update_ids()

        success_message = "\n[+] Item updated successfully."
        console.print(success_message, style=STYLE_MESSAGE_SUCCESS)

        press_enter_to_continue()


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

        message: str = (
            "Type 'ID' and then press [ENTER] to display item details or just press [ENTER] to go back:"
        )
        console.print(message, end=" ", style=STYLE_MESSAGE_WAITING)
        choise: str = input().strip()

        if not choise:
            break

        try:
            choise_int: int = int(choise)
            display_item_details(item=items[choise_int - 1])
        except:
            pass


def get_duplicate_item(item: dict) -> dict:
    """Duplicate item"""

    now: str = get_now()

    new_item: dict = {
        KEY_NAME_INSERT_TIME: now,
        KEY_NAME_UPDATE_TIME: now,
        #
        KEY_NAME_NAME: item[KEY_NAME_NAME],
        KEY_NAME_EMAIL: item[KEY_NAME_EMAIL],
        KEY_NAME_MOBILE: item[KEY_NAME_MOBILE],
        KEY_NAME_USERNAME: item[KEY_NAME_USERNAME],
        KEY_NAME_PASSWORD: item[KEY_NAME_PASSWORD],
        KEY_NAME_DESCRIPTION: item[KEY_NAME_DESCRIPTION],
    }

    return new_item


def display_item_details(item: dict) -> None:
    """Display item details"""

    while True:
        clear_screen_and_display(title="Display Item Details")

        id: int = item.get(KEY_NAME_ID, MESSAGE_NOT_SET)
        name: str = item.get(KEY_NAME_NAME, MESSAGE_NOT_SET)
        email: str = item.get(KEY_NAME_EMAIL, MESSAGE_NOT_SET)
        mobile: str = item.get(KEY_NAME_MOBILE, MESSAGE_NOT_SET)
        username: str = item.get(KEY_NAME_USERNAME, MESSAGE_NOT_SET)
        password: str = item.get(KEY_NAME_PASSWORD, MESSAGE_NOT_SET)
        description: str = item.get(KEY_NAME_DESCRIPTION, MESSAGE_NOT_SET)
        insert_time: str = item.get(KEY_NAME_INSERT_TIME, MESSAGE_NOT_SET)
        update_time: str = item.get(KEY_NAME_UPDATE_TIME, MESSAGE_NOT_SET)

        max_width: int = len(LABEL_DESCRIPTION)

        display_label(label=LABEL_ID, width=max_width)
        print(id)

        display_label(label=LABEL_NAME, width=max_width)
        print(name)

        display_label(label=LABEL_EMAIL, width=max_width)
        print(email)

        display_label(label=LABEL_MOBILE, width=max_width)
        print(mobile, f"0{mobile}", f"+98{mobile}")

        display_label(label=LABEL_USERNAME, width=max_width)
        print(username)

        display_label(label=LABEL_PASSWORD, width=max_width)
        print(password)

        display_label(label=LABEL_INSERT_TIME, width=max_width)
        print(insert_time)

        display_label(label=LABEL_UPDATE_TIME, width=max_width)
        print(update_time)

        display_label(label=LABEL_DESCRIPTION, width=max_width)
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
            case "1":
                edit_item(item=item)
            case "2":
                new_item: dict = get_duplicate_item(item=item)
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
            case _:
                break


def get_total_width() -> int:
    """Get total width"""

    total_width: int = (
        8  # Pipe Count: ('|')
        + COLUMN_WIDTH_ID
        + COLUMN_WIDTH_NAME
        + COLUMN_WIDTH_EMAIL
        + COLUMN_WIDTH_MOBILE
        + COLUMN_WIDTH_USERNAME
        + COLUMN_WIDTH_PASSWORD
        + COLUMN_WIDTH_UPDATE_TIME
    )

    return total_width


def display_table_header() -> None:
    """Display table header"""

    id: str = LABEL_ID
    name: str = "Name: URL / Application / Device"
    email: str = "Email Address"
    mobile: str = LABEL_MOBILE
    username: str = LABEL_USERNAME
    password: str = LABEL_PASSWORD
    update_time: str = "Update"

    id = id.ljust(COLUMN_WIDTH_ID, " ")
    name = name.ljust(COLUMN_WIDTH_NAME, " ")
    email = email.ljust(COLUMN_WIDTH_EMAIL, " ")
    mobile = mobile.ljust(COLUMN_WIDTH_MOBILE, " ")
    username = username.ljust(COLUMN_WIDTH_USERNAME, " ")
    password = password.ljust(COLUMN_WIDTH_PASSWORD, " ")
    update_time = update_time.ljust(COLUMN_WIDTH_UPDATE_TIME, " ")

    header: str = f"|{id}|{name}|{email}|{mobile}|{username}|{password}|{update_time}|"

    total_width: int = get_total_width()

    console.print("-" * total_width, style=STYLE_LABEL)
    console.print(header, style=STYLE_LABEL)
    console.print("-" * total_width, style=STYLE_LABEL)


def display_item_in_table_row(item: dict, display_password: bool = False) -> None:
    """Display item"""

    id: str = item.get(KEY_NAME_ID, MESSAGE_NOT_SET)
    name: str = item.get(KEY_NAME_NAME, MESSAGE_NOT_SET)
    email: str = item.get(KEY_NAME_EMAIL, MESSAGE_NOT_SET)
    mobile: str = item.get(KEY_NAME_MOBILE, MESSAGE_NOT_SET)
    username: str = item.get(KEY_NAME_USERNAME, MESSAGE_NOT_SET)
    password: str = item.get(KEY_NAME_PASSWORD, MESSAGE_NOT_SET)
    update_time: str = item.get(KEY_NAME_UPDATE_TIME, MESSAGE_NOT_SET)

    id = str(id).rjust(COLUMN_WIDTH_ID, " ")

    name = name.ljust(COLUMN_WIDTH_NAME, " ")
    email = email.ljust(COLUMN_WIDTH_EMAIL, " ")
    mobile = mobile.ljust(COLUMN_WIDTH_MOBILE, " ")
    username = username.ljust(COLUMN_WIDTH_USERNAME, " ")
    update_time = update_time.ljust(COLUMN_WIDTH_UPDATE_TIME, " ")

    update_time = update_time[0:10]

    if not display_password:
        password = "**********"
    password = password.ljust(COLUMN_WIDTH_PASSWORD, " ")

    console.print("|", style=STYLE_LABEL, end="")
    console.print(
        f"{id}|{name}|{email}|{mobile}|{username}|{password}|{update_time}", end=""
    )
    console.print("|", style=STYLE_LABEL)


def display_table_footer() -> None:
    """Display table footer"""

    total_width: int = get_total_width()
    console.print("-" * total_width, style=STYLE_LABEL)


def change_master_password() -> None:
    """Change master password"""


def display_about() -> None:
    """Display About"""


def display_main_menu() -> None:
    """Display main menu"""

    while True:
        title: str = f"Welcome to DT Password Manager - Version: {__version__}"
        clear_screen_and_display(title=title)

        menu_items: list[str] = [
            "1. Add New",
            "2. List with Password",
            "3. List without Password",
            "4. Change Master Password" "",
            "",
            "5. About",
            "",
            "Type '0' | bye | end | exit | quit | 'q' for exit...",
        ]

        choice: str = display_menu_and_get_user_prompt(
            menu_items=menu_items,
        )

        match choice.lower():
            case "1":
                add_new_item()
            case "2":
                display_items(display_password=True)
            case "3":
                display_items(display_password=False)
            case "4":
                change_master_password()
            case "5":
                display_about()
            case "0" | "bye" | "end" | "exit" | "quit" | "q":
                goodbye()


def create_sample_items() -> None:
    """Create sample items"""

    now: str = get_now()

    for index in range(5):
        item: dict = {
            KEY_NAME_INSERT_TIME: now,
            KEY_NAME_UPDATE_TIME: now,
            #
            KEY_NAME_PASSWORD: "123456",
            KEY_NAME_MOBILE: "9121087461",
            KEY_NAME_DESCRIPTION: "Nothing!",
            KEY_NAME_USERNAME: f"tasdighi_{index}",
            KEY_NAME_NAME: f"http://google.com/{index}",
            KEY_NAME_EMAIL: f"dariusht_tasdighi_{index}@gmail.com",
        }

        items.append(item)

    items[0]["description"] = "12345678901234567890"
    items[0]["password"] = "123456789012345678901234567890"

    random.shuffle(x=items)

    sort_items_by_name_and_update_ids()


def main() -> None:
    """The main of program"""

    create_sample_items()  # TODO

    display_main_menu()


if __name__ == "__main__":
    try:
        console = Console()

        items: list[dict] = []
        master_password: str = ""

        main()

    except KeyboardInterrupt:
        print()

    except Exception as error:
        print(f"\n[-] {error}!")

    print()
