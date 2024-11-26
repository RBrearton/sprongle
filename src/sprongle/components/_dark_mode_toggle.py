"""Define the DarkModeToggle component."""

from nicegui import ui


class DarkModeToggle(ui.element):
    """A toggle switch for dark mode."""

    def __init__(self) -> None:
        super().__init__()

        self.dark_mode = ui.dark_mode()

        with self.classes("flex flex-row items-center h-full"):
            ui.icon("light_mode").classes("text-2xl")
            self.switch = ui.switch(on_change=self.dark_mode.toggle).classes(
                "text-secondary"
            )
            self.switch.props["color"] = "white"
            self.switch.props("keep-color")
            ui.icon("dark_mode").classes("text-2xl")