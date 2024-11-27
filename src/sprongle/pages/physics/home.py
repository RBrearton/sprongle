"""Define the homepage for the physics section of the sprongle app."""

from sprongle._markdown_page import MarkdownPage


class PhysicsHome(MarkdownPage):
    """Homepage for the physics section of the sprongle app."""

    def __init__(self) -> None:  # noqa: D107
        super().__init__("physics", "/physics")
