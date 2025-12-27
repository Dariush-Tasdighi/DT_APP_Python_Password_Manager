"""
Application About
"""

from rich import print
from rich.console import Console
from rich.markdown import Markdown


def display_about() -> None:
    """Display about"""

    markup: str = """
# This program was developed by

- **Dariush Tasdighi**
  - Cell Phone Number: (+98)-9121087461
  - Email Address: <DariushT@GMail.com>
  - Telegram ID: <https://t.me/Dariush_Tasdighi>
  - LinkedIn: <https://www.linkedin.com/in/tasdighi>
  - Telegram Channels:
    - <https://t.me/IranianExperts>
    - <https://t.me/DT_PYTHON_LEARNING>

- **Nadia Davari**
  - Cell Phone Number: (+98)-9127289805
  - Email Address: <N.P.Davari@gmail.com>
  - LinkedIn: <https://www.linkedin.com/in/npdavari>

- **Hossein Rouzbahani**
  - Cell Phone Number: (+98)-9383995083
  - Email Address: <HR.Hossein.Rouzbahani@Gmail.com>
  - LinkedIn: <https://www.linkedin.com/in/hossein-rouzbahani>
"""

    console = Console()
    markup = markup.strip()
    markdown = Markdown(markup=markup)
    console.print(markdown)


if __name__ == "__main__":
    print("[-] This module is not meant to be run directly!")
