"""Define an admonition component."""

from typing import Self

from nicegui import ui

from sprongle import color, style


class Admonition(ui.expansion):
    """Define an admonition component."""

    def __init__(self, title: str, *, icon: str, is_open: bool) -> None:
        """Create a new admonition."""
        super().__init__(text=title, value=is_open, icon=icon)

        self.classes("w-full")
        self.classes(f"{style.bg_200}")
        self.props["header-class"] = "bg-opacity-50 dark:bg-opacity-40 "
        self.classes("border-2")
        self.classes("my-4 2xl:my-8")

    @classmethod
    def info(cls, title: str, *, is_open: bool) -> Self:
        """Create a new info admonition."""
        info = cls(
            title,
            icon="info",
            is_open=is_open,
        )

        # Because the header color has a low opacity, the background is actually
        # closer to the bg-100 color than the bg-info color. As a result, we
        # make sure to keep the text as bg-content instead of info-content.
        info.props["header-class"] += f"{style.bg_info} {style.bg_content}"
        info.classes(f"border-{color.light.info} dark:border-{color.dark.info}")
        return info

    @classmethod
    def show_working(cls) -> Self:
        """For showing working out."""
        return cls.info("Show working", is_open=True)

    @classmethod
    def success(cls, title: str, *, is_open: bool) -> Self:
        """Create a new success admonition."""
        success = cls(
            title,
            icon="check",
            is_open=is_open,
        )

        # Because the header color has a low opacity, the background is actually
        # closer to the bg-100 color than the bg-info color. As a result, we
        # make sure to keep the text as bg-content instead of info-content.
        success.props["header-class"] += (
            f"{style.bg_success} {style.bg_content}"
        )
        success.classes(
            f"border-{color.light.success} dark:border-{color.dark.success}"
        )
        return success

    @classmethod
    def show_answer(cls) -> Self:
        """For showing the answer."""
        return cls.success("Show answer", is_open=True)
