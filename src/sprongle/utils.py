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
