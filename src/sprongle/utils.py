"""Define some general utilities used in the sprongle app."""

from functools import lru_cache

from .config import parsed_config as config


@lru_cache
def get_markdown(url_name: str) -> str:
    """Return the content of a markdown file associated with a url name."""
    # Split the url name on the '/' character, and get the topic name for each
    # part of the url.
    url_names = url_name.split("/")
    topic_names = [topic_name_from_url(url) for url in url_names]

    # Now the [1:] is to remove the leading '/' character.
    markdown_path = config.pages_dir / ("/".join(topic_names)[1:])

    # If this is a path to a directory, get the home.md file.
    if markdown_path.is_dir():
        markdown_path /= "home.md"
    else:
        # If this is a path to a file, add the .md extension.
        markdown_path = markdown_path.with_suffix(".md")

    return markdown_path.read_text()


def url_from_topic_name(topic_name: str) -> str:
    """Return the relative part of the url associated with a topic name.

    For example, the directory "./Physics" is associated with the url
    "/physics". This information is captured by this function, where the input
    "Physics" is associated with the output "physics".

    More awkward onces are things like "B2: Symmetry and relativity" which is
    associated with the url "/b2".

    Please also note that topic names (e.g. "Problem set 3") are taken directly
    from directory names, and must match subdirs in the pages directory.
    """
    # If the topic name has a file extension, remove it.
    if "." in topic_name:
        topic_name = topic_name.split(".")[0]

    if topic_name == "Physics":
        return "physics"
    if topic_name == "Research":
        return "research"
    if topic_name == "B2: Symmetry and relativity":
        return "b2"
    if topic_name == "B6: Condensed matter physics":
        return "b6"

    # Anything of the form "Problem set N" is replaced with "psN".
    if topic_name.startswith("Problem set "):
        return f"ps{topic_name.split(' ')[-1]}"

    return topic_name


def topic_name_from_url(url: str) -> str:
    """Return the topic name associated with a url."""
    if url == "physics":
        return "Physics"
    if url == "research":
        return "Research"
    if url == "b2":
        return "B2: Symmetry and relativity"
    if url == "b6":
        return "B6: Condensed matter physics"

    # Anything of the form "psN" is replaced with "Problem set N".
    if url.startswith("ps"):
        return f"Problem set {url[2:]}"

    return url
