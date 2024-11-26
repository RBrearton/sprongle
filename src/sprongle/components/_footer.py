"""Define the footer used in the sprongle app."""

from nicegui import ui

from sprongle.style import bg_primary


class Footer(ui.footer):
    """The sprongle app's footer component."""

    def __init__(self) -> None:
        super().__init__(fixed=False)
        self.classes(bg_primary)

        with self:
            ui.markdown("© 2024 Dr. Richard Brearton")
