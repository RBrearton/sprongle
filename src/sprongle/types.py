"""Define some custom types for the sprongle app."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from nicegui import ui

MenuData = list["tuple[str, ui.element | MenuData]"]
