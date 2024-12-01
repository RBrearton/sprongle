"""Define the central DropdownReference component."""

from nicegui import ui

from sprongle.color import light
from sprongle.style import bg_200

from ._text import Text


class DropdownReference(ui.element):
    """The central DropdownReference component.

    This is the way that we try to get around not having equation numbers.
    """

    def __init__(self, text: str, *, ref: Text) -> None:
        """Initialize the DropdownReference component.

        Tbe text parameter is the text that we want to show in the span in which
        this reference appears. The ref is the ui element to show in the
        dropdown.
        """
        super().__init__()
        self.classes("inline")
        self.classes("flex flex-col")

        self._ref = ref
        with self:
            # Annoyingly, because of css specificity, we need to manually set
            # colors via the color and text-color prop, instead of using one of
            # our preset styles.
            self.text_chip = (
                ui.chip(text, selectable=True, selected=False)
                .props(f'color="{light.primary}"')
                .props(f'text-color="{light.primary_content}"')
            )
            with ui.card().classes().classes(bg_200) as card:
                self.card = card
                self.card.bind_visibility_from(self.text_chip, "selected")
                ui.markdown(ref.content).classes("text-xl")
                ui.button(
                    "Go to definition",
                    on_click=lambda: ui.navigate.to(self._ref),
                ).props(f'color="{light.primary}" no-caps').props(
                    f'text-color="{light.primary_content}"'
                )
