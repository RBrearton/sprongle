"""Define some scss utilities."""

import sass

from .config import parsed_config as config


def compile_scss() -> None:
    """Compile our scss to a static css file."""
    css = sass.compile(filename=str(config.scss_file))
    config.static_css_file.write_text(css)
