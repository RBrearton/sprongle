"""Define a simple Title component."""

from typing import TYPE_CHECKING, Self

from nicegui import ui

from sprongle.types import MenuData

if TYPE_CHECKING:
    from sprongle._sprongle_page import SpronglePage


class Title(ui.markdown):
    """A simple Title."""

    def __init__(self, text: str, *, level: int = 1) -> None:
        md_text = f"{'#' * level} {text}"
        super().__init__(md_text)

        self._title_text: str = text
        self.children: list[Self] = []

    def to_menu_data(self) -> tuple[str, ui.element | MenuData]:
        """Convert this title to menu data."""
        if not self.children:
            return (self._title_text, self)
        return (
            self._title_text,
            [child.to_menu_data() for child in self.children],
        )

    @classmethod
    def menu_title(
        cls, text: str, *, level: int, parent: "Self | SpronglePage"
    ) -> Self:
        """Create a menu title."""
        title = cls(text, level=level)
        if isinstance(parent, Title):
            parent.children.append(title)
        else:
            parent.titles.append(title)
        return title
