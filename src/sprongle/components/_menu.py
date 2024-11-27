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

        The subdomain should take the form /physics, /research etc. This method
        expects a "top level" subdomain.
        """
        # Make the subdomain string safe to use with the '/' operator.
        if subdomain.startswith("/"):
            subdomain = subdomain[1:]

        # Replace the subdomain with the topic name so that we can find the
        # topic on the filesystem.
        subdomain = utils.url_from_topic_name(subdomain)

        # Get all the files and directories in the subdomain other than the
        # home.md file.
        subdomain_dir = config.pages_dir / subdomain
        subtopic_paths = [
            item for item in subdomain_dir.iterdir() if item.name != "home.md"
        ]

        # Order these alphabetically by their file/directory name.
        subtopic_paths.sort(key=lambda item: item.name)

        # Create the menu.
        menu = cls(header=subdomain_dir.name)
        with menu:
            for subtopic_path in subtopic_paths:
                if subtopic_path.is_dir():
                    MenuExpansionItem.from_dir_path(subtopic_path, level=0)
                else:
                    MenuItem.from_file_path(subtopic_path)

        return menu
