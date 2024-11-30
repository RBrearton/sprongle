"""Define the central DropdownReference component."""

from nicegui import ui

from sprongle.style import bg_200

from ._text import Text


class DropdownReference(ui.dropdown_button):
    """The central DropdownReference component.

    This is the way that we try to get around not having equation numbers.
    """

    def __init__(self, text: str, *, ref: Text) -> None:
        """Initialize the DropdownReference component.

        Tbe text parameter is the text that we want to show in the span in which
        this reference appears. The ref is the ui element to show in the
        dropdown.
        """
        super().__init__(text)
        self.classes("inline")
        self.props("flat no-caps")
        self.props("dense")
        self.props(f"label={text}")
        self._ref = ref
        with self:
            with ui.card().classes().classes(bg_200):
                ui.markdown(ref.content).classes("text-xl")
                ui.button(
                    "Go to definition",
                    on_click=lambda: ui.navigate.to(self._ref),
                ).props('color="teal" no-caps')
