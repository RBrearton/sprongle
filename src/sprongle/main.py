"""Running this file runs the website."""

from nicegui import ui

from .components import Page


@ui.page("/")
def home() -> None:
    """Build the home page."""
    Page(ui.markdown("Welcome to sprongle!"))


def main() -> None:
    """Run the website."""
    ui.run()


if __name__ == "__main__":
    main()
