"""Define the MenuExpansionItem component."""

from nicegui import ui

from ._menu_item import MenuItem


class MenuExpansionItem(ui.element):
    """A menu item that expands to show more items.

    Annoyingly, nicegui doesn't have an expansion item component, so we need a
    bit more quasar than usual here.

    For more info, see https://quasar.dev/vue-components/expansion-item
    """

    def __init__(self, text: str) -> None:
        super().__init__(tag="q-expansion-item")

        # The label prop is where quasar expects the expansion item's text.
        self.props("clickable v-ripple")
        self.props(f'label="{text}"')
        self.props(':header-inset-level="0" :content-inset-level="0.5"')
        self.props("expand-separator")

        # I don't know why, but for MenuExpansionItems we can't use the
        # classes() method to add classes. Instead, we need to use the
        # header-class prop (consistent with the documentation linked above).
        # self.props('header-class="rounded-3xl"')
        # self.classes("active:bg-amber-400")
        self.props('header-class="custom-focus-helper"')

        with self:
            MenuItem("Problem set 1", "physics/b2/ps1/")
            MenuItem("Problem set 2", "physics/b2/ps2/")
            MenuItem("Problem set 3", "physics/b2/ps3/")
