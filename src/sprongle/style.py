"""Define a load of style utilities."""

from .color import light

# Tailwind classes.
_tw_menu_active = (
    f"active:bg-{light.neutral} active:text-{light.neutral_content}"
)
_tw_menu_rounded = "rounded-3xl"
_tw_header_hover = f"hover:bg-{light.secondary}"

# Menu items always occupy the full width. It makes hovering etc. way nicer.
# We never want to be able to select the text in a menu item.
# We always want them to be rounded; to change how rounded, change the
# `_tw_menu_rounded` variable.
# We also specify the active state here to make it pop a lot more when we click
# a menu item.
menu_item = f"w-full select-none {_tw_menu_rounded} {_tw_menu_active}"

header_clickable = f"{_tw_header_hover}"
