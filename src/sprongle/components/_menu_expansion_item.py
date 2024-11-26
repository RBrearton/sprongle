"""Define the MenuExpansionItem component."""

from pathlib import Path
from typing import Self

from nicegui import ui

from sprongle import style

from ._menu_item import MenuItem


class MenuExpansionItem(ui.element):
    """A menu item that expands to show more items.

    Annoyingly, nicegui doesn't have an expansion item component, so we need a
    bit more quasar than usual here.

    For more info, see https://quasar.dev/vue-components/expansion-item
    """

    def __init__(self, *, text: str, level: int) -> None:
        super().__init__(tag="q-expansion-item")

        # The label prop is where quasar expects the expansion item's text.
        self.props(f'label="{text}"')

        # Make sure the inset levels are correct.
        header_inset = level / 2
        content_inset = level + 0.5
        self.props(f':header-inset-level="{header_inset}"')
        self.props(f':content-inset-level="{content_inset}"')

        # The expand-separator is a nice touch.
        self.props("expand-separator")

        # It's really important that we only apply this to the header. We don't
        # want the dropdown contents to glow when we hover over the title!
        self.props(f'header-class="{style.menu_item}"')

    @classmethod
    def from_dir_path(cls, dir_path: Path, level: int) -> Self:
        """Create a menu expansion item from the path to a directory."""
        # Make the expansion item.
        expansion_item = cls(text=dir_path.name, level=level)

        # Now we want to add all the in the directory as menu items, and all the
        # directories as expansion items.
        with expansion_item:
            for item in dir_path.iterdir():
                if item.is_dir():
                    cls.from_dir_path(item, level + 1)
                elif item.name == "home.md":
                    # The home.md file is the default page associated with a
                    # subdomain. We don't add it to the menu.
                    continue
                else:
                    MenuItem.from_file_path(item)

        return expansion_item
