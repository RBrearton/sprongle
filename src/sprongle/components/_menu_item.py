"""Define a simple menu item that links to a page."""

from pathlib import Path
from typing import Self

from nicegui import ui

from sprongle import style
from sprongle.config import parsed_config as config
from sprongle.utils import url_from_topic_name


class MenuItem(ui.item):
    """A menu item that links to a page."""

    def __init__(self, text: str, link: str | ui.element) -> None:
        # If we were given an element, build a reference to it.
        if isinstance(link, ui.element):
            link = f"#c{link.id}"

        super().__init__(text=text, on_click=lambda: ui.navigate.to(link))

        self.props("flat")
        self.classes(style.menu_item)

    @classmethod
    def from_file_path(cls, file_path: Path) -> Self:
        """Create a menu item from the path to a file."""
        # Start by figuring out the relative path to the file in the pages dir.
        relative_path = file_path.relative_to(config.pages_dir)

        # Now we need to convert each segment of this path to its url
        # equivalent, including a "/" prefix.
        url_path = "/" + "/".join(
            url_from_topic_name(segment) for segment in relative_path.parts
        )

        # The text will be the name of the file, without the extension.
        topic_name = file_path.stem
        return cls(topic_name, url_path)

    @classmethod
    def from_menu_data(cls, item_name: str, item_to_link: ui.element) -> Self:
        """Create a menu item from a menu data tuple."""
        return cls(item_name, item_to_link)
