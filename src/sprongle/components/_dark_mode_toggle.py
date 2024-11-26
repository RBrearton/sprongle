"""Define the DarkModeToggle component."""

from nicegui import ui


class DarkModeToggle(ui.switch):
    """A toggle switch for dark mode."""

    def __init__(self) -> None:
        super().__init__()

        self.on_value_change(ui.dark_mode().toggle)
