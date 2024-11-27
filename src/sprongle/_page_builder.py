"""Define the PageBuilder class."""

from abc import ABC, abstractmethod

from nicegui import ui


class PageBuilder(ABC):
    """Implement PageBuilder to make your page visible on the sprongle app."""

    @abstractmethod
    def set_styles(self) -> None:
        """Set the styles for the page."""

    @abstractmethod
    def make_header(self) -> ui.element:
        """Build the header for the page."""

    @abstractmethod
    def make_footer(self) -> ui.element:
        """Build the footer for the page."""

    @abstractmethod
    def make_content(self) -> ui.element:
        """Build the ui element that should live in the main content area."""

    @abstractmethod
    def make_left_drawer_content(self) -> ui.element:
        """Build the ui element that should live in the left drawer."""

    @abstractmethod
    def make_right_drawer_content(self) -> ui.element | None:
        """Build the ui element that should live in the right drawer.

        This is an optional element; return None if you don't want a right
        drawer.
        """
