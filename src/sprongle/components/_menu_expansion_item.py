"""Define the MenuExpansionItem component."""

from pathlib import Path
from typing import Self

from nicegui import ui

from sprongle import style
from sprongle.types import MenuData

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
        # want the dropdown contents to glow when we hover over the title! Note
        # that these menus always appear on bg-100 backgrounds, so we set the
        # color to text-bg-content.
        self.props(f'header-class="{style.menu_item} {style.text_bg_content}"')

    @classmethod
    def from_dir_path(cls, dir_path: Path, level: int) -> Self:
        """Create a menu expansion item from the path to a directory."""
        # Make the expansion item.
        topic_name = dir_path.name
        expansion_item = cls(text=topic_name, level=level)

        # Now we want to add all the in the directory as menu items, and all the
        # directories as expansion items.
        with expansion_item:
            for subtopic_path in dir_path.iterdir():
                if subtopic_path.is_dir():
                    cls.from_dir_path(subtopic_path, level + 1)
                elif subtopic_path.name == "home.md":
                    # The home.md file is the default page associated with a
                    # subdomain. We don't add it to the menu. I'd like to handle
                    # these separately, TBD how to do that.
                    continue
                else:
                    MenuItem.from_file_path(subtopic_path)

        return expansion_item

    @classmethod
    def from_menu_data(
        cls, item_name: str, item_data: MenuData, level: int
    ) -> Self:
        """Build an expansion item from a menu data tuple."""
        # Make the expansion item.
        expansion_item = cls(text=item_name, level=level)

        # Now add all the items in the data as child menu items or expansion
        # items.
        for sub_item_name, sub_item_data in item_data:
            if isinstance(sub_item_data, list):
                cls.from_menu_data(sub_item_name, sub_item_data, level + 1)
            else:
                MenuItem.from_menu_data(sub_item_name, sub_item_data)

        return expansion_item
