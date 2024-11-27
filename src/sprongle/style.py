"""Define a load of style utilities."""

from .color import dark, light

# Tailwind classes.
# Menu items.
_tw_menu_active = (
    f"active:bg-{light.neutral} "
    f"active:text-{light.neutral_content} "
    f"hover:bg-{light.base_300} "
)
rounded = "rounded-3xl"

# Header items.
_tw_header_hover = (
    f"text-{light.primary_content} "
    f"hover:bg-{light.base_200} hover:bg-opacity-30"
)
_tw_header_active = f"active:bg-{light.base_100} active:bg-opacity-40"


# Some simple convenience auto dark mode classes.
bg_100 = f"bg-{light.base_100} dark:bg-{dark.base_100}"
bg_200 = f"bg-{light.base_200} dark:bg-{dark.base_200}"
bg_300 = f"bg-{light.base_300} dark:bg-{dark.base_300}"
text_bg_content = f"text-{light.base_content} dark:text-{dark.base_content}"
bg_primary = (
    f"bg-{light.primary} dark:bg-{dark.primary}"
    f" text-{light.primary_content} dark:text-{dark.primary_content}"
)
bg_info = (
    f"bg-{light.info} dark:bg-{dark.info} "
    f"text-{light.info_content} dark:text-{dark.info_content}"
)
bg_success = (
    f"bg-{light.success} dark:bg-{dark.success} "
    f"text-{light.success_content} dark:text-{dark.success_content}"
)
bg_warning = (
    f"bg-{light.warning} dark:bg-{dark.warning} "
    f"text-{light.warning_content} dark:text-{dark.warning_content}"
)
bg_error = (
    f"bg-{light.error} dark:bg-{dark.error} "
    f"text-{light.error_content} dark:text-{dark.error_content}"
)

# Menu items always occupy the full width. It makes hovering etc. way nicer.
# We never want to be able to select the text in a menu item.
# We always want them to be rounded; to change how rounded, change the
# `_tw_menu_rounded` variable.
# We also specify the active state here to make it pop a lot more when we click
# a menu item.
menu_item = f"w-full select-none {rounded} {_tw_menu_active} {text_bg_content}"

header_clickable = f"{_tw_header_hover} {_tw_header_active}"
