"""Running this file runs the website."""

from collections.abc import Callable

from fastapi import Request
from fastapi.responses import HTMLResponse
from nicegui import app, ui

from . import components as c
from .config import parsed_config as config
from .scss_utils import compile_scss
from .style import bg_100, text_bg_content
from .utils import get_markdown


def page_template(subdomain: str) -> tuple[ui.element, ui.element]:
    """Build the page template.

    This function builds the core page components that are shared across all
    pages on the website. It returns a tuple where the first element is a very
    basic central div covering the entire central area, and the second element
    is a content area that is centered and has a max width for nice content
    display.
    """
    # This is needed for the github logo.
    eva_icons = "https://unpkg.com/eva-icons@1.1.3/style/eva-icons.css"
    ui.add_head_html(f'<link href={eva_icons} rel="stylesheet" />')
    ui.page_title("Sprongle")

    # Add our static styles.css file. This is built automatically from our
    # assets/styles.scss file.
    ui.add_head_html(
        f'<link rel= "stylesheet" href="/{config.static_dir_name}/styles.css">'
    )

    # Now build the core page components.
    c.Header(title="Sprongle")
    with c.LeftDrawer():
        c.Menu.from_subdomain(subdomain)
    c.RightDrawer()
    c.Footer()

    # The central div left aligns content with no padding. This is the simplest
    # thing we could let users work with.
    central_div = ui.element().classes(
        f"w-full h-full {bg_100} {text_bg_content} min-h-screen"
    )

    # We also want to make a neat material-mkdocs style content area with a
    # central alignment and a fixed max width for nice blog-style content.
    with central_div:
        # Make a pure alignment div.
        with ui.element().classes(
            "flex flex-col justify-start items-center w-full"
        ):
            # max-w-850px says that this should never exceed 850px.
            # w-full encourages the div to reach exactly that width, even if the
            # content isn't particularly wide. This keeps sizes consistent.
            # flex-shrink makes this div shrinkable when screen space decreases.
            content_area = ui.element().classes(
                "max-w-[850px] w-full flex-shrink py-6"
            )

    return central_div, content_area


@app.middleware("http")
async def clear_cache_if_auto_reloading(
    request: Request,
    call_next: Callable,  # type: ignore  # noqa: PGH003
) -> HTMLResponse:
    """Clear the cache if auto-reloading is enabled.

    This middleware is used to clear the cache of the render_markdown function
    if auto-reloading is enabled. This is useful for development purposes, as it
    means that changes to the markdown files will be immediately reflected in
    the rendered HTML.
    """
    if config.auto_reload:
        get_markdown.cache_clear()
    return await call_next(request)  # type: ignore  # noqa: PGH003


@ui.page("/")
def home() -> None:
    """Build the home page."""
    _, content_area = page_template("/physics")

    with content_area:
        ui.markdown("Welcome to sprongle!")


@ui.page("/physics")
def physics() -> None:
    """Build the physics page."""
    # Currently this is the same as the home page.
    _, content_area = page_template("/physics")
    with content_area:
        ui.markdown(get_markdown("/physics"))


def main() -> None:
    """Run the website."""
    # Make sure that our static directory is being served.
    app.add_static_files(
        url_path=f"/{config.static_dir_name}",
        local_directory=config.static_dir_path,
    )

    # Run the website.
    ui.run(
        fastapi_docs=True, show=False, reload=config.auto_reload, favicon="🤓"
    )


# Every time we reload the page, make sure that we recompile the scss.
compile_scss()
main()
