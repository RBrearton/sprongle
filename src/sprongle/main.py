"""Running this file runs the website."""

from collections.abc import Callable

from fastapi import Request
from fastapi.responses import HTMLResponse
from nicegui import app, ui

from ._markdown_page import MarkdownPage
from .config import parsed_config as config
from .pages.physics.b2.problem_set_2 import B2ProblemSet2
from .pages.physics.b2.problem_set_3 import B2ProblemSet3
from .pages.physics.b2.problem_set_4 import B2ProblemSet4
from .pages.physics.b6.problem_set_2 import B6ProblemSet2
from .scss_utils import compile_scss
from .utils import get_markdown


@app.middleware("http")
async def clear_cache_if_auto_reloading(
    request: Request,
    call_next: Callable,  # type: ignore
) -> HTMLResponse:
    """Clear the cache if auto-reloading is enabled.

    This middleware is used to clear the cache of the render_markdown function
    if auto-reloading is enabled. This is useful for development purposes, as it
    means that changes to the markdown files will be immediately reflected in
    the rendered HTML.
    """
    if config.auto_reload:
        get_markdown.cache_clear()
    return await call_next(request)  # type: ignore


@ui.page("/")
def home() -> None:
    """Build the home page."""
    # Currently, as there's no other subdomain, we give the home page the
    # physics subdomain so that we build the same left drawer as we would
    # for anything in the physics section.
    page = MarkdownPage(subdomain_name="physics", page_path="/")
    page.make_entire_page()


@ui.page("/physics")
def physics() -> None:
    """Build the physics page."""
    page = MarkdownPage(subdomain_name="physics", page_path="/physics")
    page.make_entire_page()


@ui.page("/physics/b2/ps2")
def b2_ps2() -> None:
    """Build the B2 PS2 page."""
    B2ProblemSet2().make_entire_page()


@ui.page("/physics/b2/ps3")
def b2_ps3() -> None:
    """Build the B2 PS3 page."""
    B2ProblemSet3().make_entire_page()


@ui.page("/physics/b2/ps4")
def b2_ps4() -> None:
    """Build the B2 PS4 page."""
    B2ProblemSet4().make_entire_page()


@ui.page("/physics/b6/ps2")
def b6_ps2() -> None:
    """Build the B6 PS2 page."""
    B6ProblemSet2().make_entire_page()


def main() -> None:
    """Run the website."""
    # Make sure that our static directory is being served.
    app.add_static_files(
        url_path=f"/{config.static_dir_name}",
        local_directory=config.static_dir_path,
    )

    # Run the website.
    ui.run(
        fastapi_docs=True,
        show=False,
        reload=config.auto_reload,
        favicon="🤓",
        storage_secret=config.storage_secret,
        port=config.port,
    )


# Every time we reload the page, make sure that we recompile the scss.
compile_scss()
main()
