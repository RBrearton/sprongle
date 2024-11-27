"""Define the menu component."""

from typing import Self

from nicegui import ui

from sprongle import utils
from sprongle.config import parsed_config as config

from ._menu_expansion_item import MenuExpansionItem
from ._menu_header import MenuHeader
from ._menu_item import MenuItem


class Menu(ui.list):
    """The sprongle app's menu component."""

    def __init__(self, *, header: str) -> None:
        super().__init__()

        self.classes("w-full rounded-borders")
        self.classes("sticky top-0")

        with self:
            MenuHeader(header)

    @classmethod
    def from_subdomain(cls, subdomain: str) -> Self:
        """Create a menu from the subdomain passed as an argument.

        This is cached, so whenever a brand new page is added, you'll need to
        restart the app to see it in the menu.
        """
        # Make the subdomain string safe to use with the '/' operator.
        if subdomain.startswith("/"):
            subdomain = subdomain[1:]

        # Get all the files and directories in the subdomain other than the
        # home.md file.
        subdomain_dir = config.pages_dir / subdomain
        subdomain_dir = utils.get_case_sensitive_path(subdomain_dir)
        print(f"Found {subdomain_dir}")

        subdomain_contents = [
            item for item in subdomain_dir.iterdir() if item.name != "home.md"
        ]

        # Order these alphabetically by their file/directory name.
        subdomain_contents.sort(key=lambda item: item.name)

        # Create the menu.
        menu = cls(header=subdomain_dir.name)
        with menu:
            for item in subdomain_contents:
                if item.is_dir():
                    MenuExpansionItem.from_dir_path(item, level=0)
                else:
                    MenuItem.from_file_path(item)

        return menu
