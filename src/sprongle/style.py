"""Define a load of style utilities."""

from .color import light

# Tailwind classes.
# Menu items.
_tw_menu_active = (
    f"active:bg-{light.neutral} active:text-{light.neutral_content} "
    f"hover:bg-{light.base_300}"
)
_tw_menu_rounded = "rounded-3xl"

# Header items.
_tw_header_hover = (
    f"text-{light.primary_content} "
    f"hover:bg-{light.secondary} hover:opacity-30"
)

# Menu items always occupy the full width. It makes hovering etc. way nicer.
# We never want to be able to select the text in a menu item.
# We always want them to be rounded; to change how rounded, change the
# `_tw_menu_rounded` variable.
# We also specify the active state here to make it pop a lot more when we click
# a menu item.
menu_item = f"w-full select-none {_tw_menu_rounded} {_tw_menu_active}"

header_clickable = f"{_tw_header_hover}"
