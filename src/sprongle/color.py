"""Define the colors used in the sprongle app.

This module is heavily inspired by the way that DaisyUI defines its colors.
"""

from pydantic import BaseModel


class ColorSchemeModel(BaseModel):
    """The model that defines all the colors that can be used in the app.

    All colors must be valid tailwindcss colors.

    Any color that ends in "_content" is the color that should be used for text
    on top of the corresponding color. For example, the "primary_content" color
    should be used for text on top of the "primary" color.
    """

    primary: str
    primary_content: str

    secondary: str
    secondary_content: str

    accent: str
    accent_content: str

    neutral: str
    neutral_content: str

    base_100: str
    base_200: str
    base_300: str
    base_content: str

    info: str
    info_content: str

    success: str
    success_content: str

    warning: str
    warning_content: str

    error: str
    error_content: str


light = ColorSchemeModel(
    primary="teal-600",
    primary_content="gray-50",
    secondary="amber-400",
    secondary_content="gray-950",
    accent="violet-400",
    accent_content="gray-950",
    neutral="slate-900",
    neutral_content="gray-200",
    base_100="stone-200",
    base_200="stone-300",
    base_300="stone-400",
    base_content="gray-950",
    info="sky-500",
    info_content="gray-950",
    success="green-500",
    success_content="gray-950",
    warning="yellow-500",
    warning_content="gray-950",
    error="red-500",
    error_content="gray-950",
)

dark = ColorSchemeModel(
    primary="teal-600",
    primary_content="gray-50",
    secondary="pink-400",
    secondary_content="pink-950",
    accent="amber-400",
    accent_content="amber-950",
    neutral="slate-900",
    neutral_content="neutral-200",
    base_100="zinc-800",
    base_200="zinc-900",
    base_300="zinc-950",
    base_content="neutral-200",
    info="sky-500",
    info_content="sky-950",
    success="green-500",
    success_content="green-950",
    warning="yellow-500",
    warning_content="yellow-950",
    error="red-500",
    error_content="red-950",
)
