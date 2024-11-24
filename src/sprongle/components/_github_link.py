"""Defines the GitHub link component."""

from nicegui import ui

from sprongle import style


class GithubLink(ui.element):
    """The sprongle app's GitHub link component."""

    def __init__(self) -> None:
        super().__init__(tag="q-btn")

        self.on(
            "click",
            lambda: ui.navigate.to(
                "https://github.com/RBrearton/sprongle", new_tab=True
            ),
        )

        # Make the github icon button round and flat.
        self.props('icon="eva-github"')
        self.props("round flat")

        # Set the size and style.
        self.classes("text-xl")
        self.classes(style.header_clickable)

        with self:
            ui.tooltip("Source code here :)")
