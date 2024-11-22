"""Defines the GitHub link component."""

from nicegui import ui


class GithubLink(ui.button):
    """The sprongle app's GitHub link component."""

    def __init__(self) -> None:
        super().__init__(
            icon="eva-github",
            on_click=lambda: ui.navigate.to(
                "https://github.com/RBrearton/sprongle",
                new_tab=True,
            ),
        )

        # Make the icon button round, and without a background.
        self.props("round flat")
        self.classes("text-white")

        with self:
            ui.tooltip("Source code here :)")
