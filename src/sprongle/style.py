"""Define a load of style utilities."""

from .color import dark, light

# Tailwind classes.
# Menu items.
_tw_menu_active = (
    f"active:bg-{light.neutral} "
    f"active:text-{light.neutral_content} "
    f"hover:bg-{light.base_300} "
)
_tw_menu_rounded = "rounded-3xl"

# Header items.
_tw_header_hover = (
    f"text-{light.primary_content} "
    f"hover:bg-{light.base_200} hover:bg-opacity-30"
)
_tw_header_active = f"active:bg-{light.base_100} active:bg-opacity-40"

# Menu items always occupy the full width. It makes hovering etc. way nicer.
# We never want to be able to select the text in a menu item.
# We always want them to be rounded; to change how rounded, change the
# `_tw_menu_rounded` variable.
# We also specify the active state here to make it pop a lot more when we click
# a menu item.
menu_item = f"w-full select-none {_tw_menu_rounded} {_tw_menu_active}"

header_clickable = f"{_tw_header_hover} {_tw_header_active}"

# Some simple convenience auto dark mode classes.
bg_100 = f"bg-{light.base_100} dark:bg-{dark.base_100}"
bg_200 = f"bg-{light.base_200} dark:bg-{dark.base_200}"
bg_300 = f"bg-{light.base_300} dark:bg-{dark.base_300}"
bg_primary = (
    f"bg-{light.primary} dark:bg-{dark.primary}"
    f" text-{light.primary_content} dark:text-{dark.primary_content}"
)
