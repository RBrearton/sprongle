"""Define an admonition component."""

from typing import Self

from nicegui import ui


class Admonition(ui.expansion):
    """Define an admonition component."""

    def __init__(self, title: str, *, icon: str, is_open: bool) -> None:
        """Create a new admonition."""
        super().__init__(text=title, value=is_open, icon=icon)

        self.classes("w-full")

    @classmethod
    def info(cls, title: str, *, is_open: bool) -> Self:
        """Create a new info admonition."""
        return cls(title, icon="info", is_open=is_open)

    @classmethod
    def show_working(cls) -> Self:
        """For showing working out."""
        return cls.info("Show working", is_open=False)
