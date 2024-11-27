"""The site's homepage."""

from sprongle._markdown_page import MarkdownPage


class Home(MarkdownPage):
    """The site's homepage."""

    def __init__(self) -> None:  # noqa: D107
        # Currently, as there's no other subdomain, we give the home page the
        # physics subdomain so that we build the same left drawer as we would
        # for anything in the physics section.
        super().__init__("physics", "/")
