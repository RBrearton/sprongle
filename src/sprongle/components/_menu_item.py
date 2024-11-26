"""Define a simple menu item that links to a page."""

from pathlib import Path
from typing import Self

from nicegui import ui

from sprongle import style
from sprongle.config import parsed_config as config


class MenuItem(ui.item):
    """A menu item that links to a page."""

    def __init__(self, text: str, link: str) -> None:
        super().__init__(text=text, on_click=lambda: ui.navigate.to(link))

        self.props("flat")
        self.classes(style.menu_item)

    @classmethod
    def from_file_path(cls, file_path: Path) -> Self:
        """Create a menu item from the path to a file."""
        # The start of the path has to be the same as the config.pages_dir. The
        # link that we generate will be the path relative to the pages_dir.
        # Get the relative path to the file.
        relative_path = str(file_path.relative_to(config.pages_dir))

        # Make sure that the relative path takes the form /relative/path.
        # Obviously this wouldn't normally be a valid relative path, but we're
        # providing a link to a page on our website.
        relative_path = f"/{relative_path}"

        # The text will be the name of the file, without the extension.
        text = file_path.stem
        return cls(text, str(relative_path))
