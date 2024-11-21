"""Running this file runs the website."""

from nicegui import ui

from . import components as c


def page_template() -> None:
    """Build the page template."""
    ui.add_head_html(
        '<link href="https://unpkg.com/eva-icons@1.1.3/style/eva-icons.css" rel="stylesheet" />'  # noqa: E501
    )

    c.Header(title="Sprongle")
    c.LeftDrawer()
    c.RightDrawer()


@ui.page("/")
def home() -> None:
    """Build the home page."""
    page_template()
    ui.markdown("Welcome to sprongle!")


def main() -> None:
    """Run the website."""
    ui.run()


main()
