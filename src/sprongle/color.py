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
    secondary="sky-600",
    secondary_content="gray-50",
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
    primary=light.primary,
    primary_content=light.primary_content,
    secondary=light.secondary,
    secondary_content=light.secondary_content,
    accent=light.accent,
    accent_content=light.accent_content,
    neutral="slate-900",
    neutral_content="neutral-200",
    base_100="gray-700",
    base_200="gray-800",
    base_300="gray-900",
    base_content="gray-300",
    info=light.info,
    info_content=light.info_content,
    success=light.success,
    success_content=light.success_content,
    warning=light.warning,
    warning_content=light.warning_content,
    error=light.error,
    error_content=light.error_content,
)
