"""Define the menu component."""

from typing import Self

from nicegui import ui

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
    def from_physics_subdomain(cls) -> Self:
        """Create the menu for the physics subdomain."""
        menu = cls(header="Physics")
        with menu:
            with MenuExpansionItem(text="B2: Symmetry and relativity", level=0):
                MenuItem(text="Problem set 2", link="/physics/b2/ps2")
                MenuItem(text="Problem set 3", link="/physics/b2/ps3")
                MenuItem(text="Problem set 4", link="/physics/b2/ps4")
            with MenuExpansionItem(
                text="B6: Condensed matter physics", level=0
            ):
                MenuItem(text="Problem set 2", link="/physics/b6/ps2")

        return menu

    @classmethod
    def from_subdomain(cls, subdomain: str) -> Self:
        """Create a menu from the subdomain passed as an argument.

        The subdomain should take the form /physics, /research etc. This method
        expects a "top level" subdomain.
        """
        # We should do the same thing whether or not the subdomain has a leading
        # slash.
        if subdomain.startswith("/"):
            subdomain = subdomain[1:]

        if subdomain.lower() == "physics":
            return cls.from_physics_subdomain()

        return cls(header="Unknown subdomain")
