"""Define a simple Text component."""

from nicegui import ui


class Text(ui.markdown):
    """A simple text component."""

    def __init__(self, text: str) -> None:
        super().__init__(
            text,
            extras=[
                "fenced-code-blocks",
                "tables",
                "latex",
            ],
        )
