"""Running this file runs the website."""

from nicegui import app, ui

from . import components as c
from .config import parsed_config as config
from .scss_utils import compile_scss


def page_template() -> None:
    """Build the page template."""
    # This is needed for the github logo.
    eva_icons = "https://unpkg.com/eva-icons@1.1.3/style/eva-icons.css"
    ui.add_head_html(f'<link href={eva_icons} rel="stylesheet" />')

    # Add our static styles.css file. This is built automatically from our
    # assets/styles.scss file.
    ui.add_head_html(
        f'<link rel= "stylesheet" href="/{config.static_dir_name}/styles.css">'
    )

    # Now build the core page components.
    c.Header(title="Sprongle")
    c.LeftDrawer()
    c.RightDrawer()
    ui.query("q-focus-helper").classes("active:bg-amber-400")


@ui.page("/")
def home() -> None:
    """Build the home page."""
    page_template()
    ui.markdown("Welcome to sprongle!")
    ui.button("defaults")


def main() -> None:
    """Run the website."""
    # Make sure that our static directory is being served.
    app.add_static_files(
        url_path=f"/{config.static_dir_name}",
        local_directory=config.static_dir_path,
    )

    # Run the website.
    ui.run()


# Every time we reload the page, make sure that we recompile the scss.
compile_scss()
main()
