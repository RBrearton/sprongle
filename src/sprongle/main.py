"""Running this file runs the website."""

from nicegui import ui

from .components import Header, HeaderButton


def page_template() -> None:
    """Build the page template."""
    Header(title="Sprongle")


@ui.page("/")
def home() -> None:
    """Build the home page."""
    page_template()
    ui.markdown("Welcome to sprongle!")


def main() -> None:
    """Run the website."""
    ui.run()


main()
