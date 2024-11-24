"""Contains the definition of the app's config."""

from pathlib import Path

from pydantic import DirectoryPath, FilePath
from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    """The app's configuration is defined by this class."""

    static_dir: DirectoryPath = Path(__file__).parent.parent.parent / "static"
    assets_dir: DirectoryPath = Path(__file__).parent.parent.parent / "assets"
    scss_file: FilePath = assets_dir / "styles.scss"

    model_config = SettingsConfigDict(env_prefix="sprongle_")


parsed_config = Config()
"""This is parsed when the app starts up.

Optionally, users can also instantiate Config() manually to get an up-to-date
config object, at the cost of a small performance hit.
"""
