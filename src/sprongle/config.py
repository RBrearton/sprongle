"""Contains the definition of the app's config."""

from pathlib import Path

from pydantic import DirectoryPath, FilePath
from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    """The app's configuration is defined by this class."""

    auto_reload: bool = True

    # Define some file and directory names.
    static_dir_name: str = "static"
    assets_dir_name: str = "assets"
    styles_css_name: str = "styles.css"
    styles_scss_name: str = "styles.scss"
    pages_dir_name: str = "pages"

    # Define some paths to important files and directories.
    project_dir: DirectoryPath = Path(__file__).parent.parent.parent
    pages_dir: DirectoryPath = project_dir / pages_dir_name
    static_dir_path: DirectoryPath = project_dir / static_dir_name
    assets_dir: DirectoryPath = project_dir / assets_dir_name
    scss_file: FilePath = assets_dir / styles_scss_name
    static_css_file: FilePath = static_dir_path / styles_css_name

    # The secret for the storage.
    storage_secret: str = "sprongle"

    # The settings config.
    model_config = SettingsConfigDict(env_prefix="sprongle_")


parsed_config = Config()
"""This is parsed when the app starts up.

Optionally, users can also instantiate Config() manually to get an up-to-date
config object, at the cost of a small performance hit.
"""
