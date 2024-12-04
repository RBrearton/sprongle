"""Define the SpronglePage class."""

from typing import TYPE_CHECKING

from nicegui import ui

from . import components as c
from ._page_builder import PageBuilder
from .color import dark_base_100
from .config import parsed_config as config
from .style import bg_100, bg_content

if TYPE_CHECKING:
    from .types import MenuData


class SpronglePage(PageBuilder):
    """A page builder with some defaults set for the sprongle app."""

    def __init__(self, subdomain_name: str) -> None:
        self._subdomain_name = subdomain_name

        # This is what we use to recursively build the right menu.
        self.titles: list[c.Title] = []
        self._right_menu_data: MenuData = []

    def make_header(self) -> None:
        # This is needed for the github logo.
        eva_icons = "https://unpkg.com/eva-icons@1.1.3/style/eva-icons.css"
        ui.add_head_html(f'<link href={eva_icons} rel="stylesheet" />')
        ui.query("body").classes(bg_100)
        ui.colors(dark_page=dark_base_100)

        # Set the page title. This is what you see when you hover over the tab
        # in a browser.
        ui.page_title("s p r o n g l e")

        # Add our static styles.css file. This is built automatically from our
        # assets/styles.scss file.
        styles_ref = f"/{config.static_dir_name}/styles.css"
        ui.add_head_html(f'<link rel= "stylesheet" href="{styles_ref}">')

    def make_navbar(self) -> c.Header:
        return c.Header(title="Sprongle.com")

    def make_footer(self) -> ui.element:
        return c.Footer()

    def make_left_drawer(self) -> c.LeftDrawer:
        return c.LeftDrawer()

    def make_right_drawer(self) -> ui.element:
        return c.RightDrawer()

    def make_right_drawer_content(self) -> ui.element | None:
        # If there's nothing to put in the drawer, return None.
        if not self._right_menu_data and not self.titles:
            return None

        # If we were given titles, build the menu from them.
        if self.titles:
            self._right_menu_data = [
                title.to_menu_data() for title in self.titles
            ]

        # Otherwise, build the menu!
        right_menu = c.Menu(header="Contents")
        with right_menu:
            for menu_item in self._right_menu_data:
                item_name, item_data = menu_item
                if isinstance(item_data, list):
                    c.MenuExpansionItem.from_menu_data(item_name, item_data, 0)
                else:
                    c.MenuItem.from_menu_data(item_name, item_data)

    def make_left_drawer_content(self) -> ui.element:
        return c.Menu.from_subdomain(self._subdomain_name)

    def make_entire_page(self) -> None:
        self.make_header()
        navbar = self.make_navbar()
        self.make_footer()
        with self.make_left_drawer() as left_drawer:
            self.make_left_drawer_content()
            navbar.set_drawer_ref(left_drawer)

        # The central div left aligns content with no padding.
        central_div = ui.element().classes(
            f"w-full h-full {bg_100} {bg_content} min-h-screen"
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
                # space decreases. Finally, we make it an article to improve
                # text formatting.
                content_area = (
                    ui.element(tag="article")
                    .classes("max-w-[850px] w-full flex-shrink py-6")
                    .classes("text-md 2xl:text-lg")
                )
                with content_area:
                    self.make_content()

        # The right drawer is optional. We make it last so that, if make_content
        # is used to populate data needed to make the right drawer, it's ready.
        right_drawer = self.make_right_drawer()
        with right_drawer:
            self.make_right_drawer_content()
