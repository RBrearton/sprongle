"""Define the menu component."""

from nicegui import ui

from ._menu_expansion_item import MenuExpansionItem
from ._menu_header import MenuHeader


class Menu(ui.list):
    """The sprongle app's menu component."""

    def __init__(self) -> None:
        super().__init__()

        self.classes("w-full rounded-borders")

        with self:
            MenuHeader("Physics")
            MenuExpansionItem("B2: Symmetry and relativity")
            MenuExpansionItem("B6: Condensed matter physics")
