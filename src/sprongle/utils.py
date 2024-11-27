"""Define some general utilities used in the sprongle app."""

from pathlib import Path


def get_case_sensitive_path(path: Path) -> Path:
    """Given a Path object, return the case-correct version of the path."""

    def get_err(path: Path) -> FileNotFoundError:
        return FileNotFoundError(f"The path {path} does not exist.")

    parts = path.parts
    correct_parts: list[str] = []

    for part in parts:
        if not correct_parts:
            # This is the root part (e.g., '/', 'C:\\')
            correct_parts.append(part)
        else:
            # Get the directory contents
            parent_dir = Path(*correct_parts)
            children = [child.name for child in parent_dir.iterdir()]
            matching_child = next(
                (child for child in children if child.lower() == part.lower()),
                None,
            )

            # Make sure the child exists.
            if matching_child is None:
                raise get_err(Path(*correct_parts, part))

            # Add the child to the correct parts.
            correct_parts.append(matching_child)

    return Path(*correct_parts)


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
