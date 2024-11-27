"""Define the central DropdownReference component."""

from nicegui import ui


class HoverReference(ui.tooltip):
    """The central DropdownReference component.

    This is the way that we try to get around not having equation numbers.
    """

    def __init__(self, *, ref: ui.element) -> None:
        super().__init__()
        self._ref = ref
