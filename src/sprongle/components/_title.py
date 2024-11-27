"""Define a simple Title component."""

from typing import Self

from nicegui import ui


class Title(ui.html):
    """A simple Title."""

    def __init__(self, text: str, *, level: int = 1) -> None:
        super().__init__(tag=f"h{level}", content=text)

        self.children: list[ui.element] = []

    @classmethod
    def menu_title(cls, text: str, level: int, *, parent: Self | None) -> Self:
        """Create a menu title."""
        title = cls(text, level=level)
        if parent:
            parent.children.append(title)
        return title
