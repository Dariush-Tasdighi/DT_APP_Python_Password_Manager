"""
Application Constants
"""

from pathlib import Path
from rich.style import Style

# Start: You can change these values
DEFAULT_EMAIL: str = "dariusht@gmail.com"
DEFAULT_MOBILE: str = "9121087461"
DEFAULT_USERNAME: str = "dariusht"
GENERATED_PASSWORD_LENGTH: int = 24

DATA_FILE_PATH: Path = Path("./data.bin")
# End: You can change these values

DATE_TIME_FORMAT: str = "%Y-%m-%d %H:%M:%S"
BACKUP_FILE_FORMAT: str = "%Y_%m_%d_%H_%M_%S"

COLUMN_WIDTH_ID: int = 3
COLUMN_WIDTH_NAME: int = 40
COLUMN_WIDTH_EMAIL: int = 32
COLUMN_WIDTH_MOBILE: int = 11
COLUMN_WIDTH_PASSWORD: int = 32
COLUMN_WIDTH_USERNAME: int = 20
COLUMN_WIDTH_UPDATE_TIME: int = 10

KEY_NAME_ID: str = "id"
LABEL_ID: str = KEY_NAME_ID.upper()

KEY_NAME_NAME: str = "name"
LABEL_NAME: str = KEY_NAME_NAME.title()

KEY_NAME_EMAIL: str = "email"
LABEL_EMAIL: str = KEY_NAME_EMAIL.title()

KEY_NAME_MOBILE: str = "mobile"
LABEL_MOBILE: str = KEY_NAME_MOBILE.title()

KEY_NAME_USERNAME: str = "username"
LABEL_USERNAME: str = KEY_NAME_USERNAME.title()

KEY_NAME_PASSWORD: str = "password"
LABEL_PASSWORD: str = KEY_NAME_PASSWORD.title()

KEY_NAME_DESCRIPTION: str = "description"
LABEL_DESCRIPTION: str = KEY_NAME_DESCRIPTION.title()

KEY_NAME_INSERT_TIME: str = "insert_time"
LABEL_INSERT_TIME: str = KEY_NAME_INSERT_TIME.replace("_", " ").title()

KEY_NAME_UPDATE_TIME: str = "update_time"
LABEL_UPDATE_TIME: str = KEY_NAME_UPDATE_TIME.replace("_", " ").title()

MESSAGE_NOT_SET: str = "[NOT SET]"

STYLE_MESSAGE_ERROR = Style(color="red", blink=False, bold=True)
STYLE_MESSAGE_WAITING = Style(color="cyan", blink=False, bold=True)
STYLE_MESSAGE_SUCCESS = Style(color="green", blink=False, bold=True)

STYLE_COLUMN_HEADER = Style(color="blue", blink=False, bold=True)
STYLE_LABEL = Style(color="green_yellow", blink=False, bold=True)
STYLE_MENU_ITEM = Style(color="green_yellow", blink=False, bold=True)


if __name__ == "__main__":
    print("[-] This module is not meant to be run directly!")
