"""Define the SpronglePage class."""

from nicegui import ui

from . import components as c
from ._page_builder import PageBuilder
from .config import parsed_config as config
from .style import bg_100, text_bg_content


class SpronglePage(PageBuilder):
    """A page builder with some defaults set for the sprongle app."""

    def __init__(self, subdomain_name: str) -> None:
        self._subdomain_name = subdomain_name

    def make_header(self) -> None:
        # This is needed for the github logo.
        eva_icons = "https://unpkg.com/eva-icons@1.1.3/style/eva-icons.css"
        ui.add_head_html(f'<link href={eva_icons} rel="stylesheet" />')

        # Set the page title. This is what you see when you hover over the tab
        # in a browser.
        ui.page_title("Sprongle")

        # Add our static styles.css file. This is built automatically from our
        # assets/styles.scss file.
        styles_ref = f"/{config.static_dir_name}/styles.css"
        ui.add_head_html(f'<link rel= "stylesheet" href="{styles_ref}">')

    def make_navbar(self) -> ui.element:
        return c.Header(title="Sprongle")

    def make_footer(self) -> ui.element:
        return c.Footer()

    def make_left_drawer(self) -> ui.element:
        return c.LeftDrawer()

    def make_right_drawer(self) -> ui.element:
        return c.RightDrawer()

    def make_left_drawer_content(self) -> ui.element:
        return c.Menu.from_subdomain(self._subdomain_name)

    def make_entire_page(self) -> None:
        self.make_header()
        self.make_navbar()
        self.make_footer()
        with self.make_left_drawer():
            self.make_left_drawer_content()

        # The right drawer is optional.
        right_drawer = self.make_right_drawer()
        with right_drawer:
            self.make_right_drawer_content()

        # The central div left aligns content with no padding.
        central_div = ui.element().classes(
            f"w-full h-full {bg_100} {text_bg_content} min-h-screen"
        )

        # We also want to make a neat material-mkdocs style content area with a
        # central alignment and a fixed max width for nice blog-style content.
        with central_div:
            # Make a pure alignment div with a little padding.
            with ui.element().classes(
                "flex flex-col justify-start items-center w-full p-4"
            ):
                # max-w-850px says that this should never exceed 850px.
                # w-full encourages the div to reach exactly that width, even if
                # the content isn't particularly wide. This keeps sizes
                # consistent. flex-shrink makes this div shrinkable when screen
                # space decreases.
                content_area = ui.element().classes(
                    "max-w-[850px] w-full flex-shrink py-6"
                )
                with content_area:
                    self.make_content()
