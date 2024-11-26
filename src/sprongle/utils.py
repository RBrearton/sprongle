"""Define some general utilities used in the sprongle app."""

from pathlib import Path


def get_case_correct_path(path: Path) -> Path:
    """Given a Path object, return the case-correct version of the path."""

    def get_err(path: Path) -> FileNotFoundError:
        return FileNotFoundError(f"The path {path} does not exist.")

    if not path.exists():
        raise get_err(path)

    parts = path.parts
    correct_parts: list[str] = []

    for part in parts:
        if not correct_parts:
            # This is the root part (e.g., '/', 'C:\\')
            correct_parts.append(part)
        else:
            # Get the directory contents
            parent_dir = Path(*correct_parts)
            try:
                # Find the correct case for the current part
                correct_part = next(
                    item
                    for item in parent_dir.iterdir()
                    if item.name.lower() == part.lower()
                ).name
                correct_parts.append(correct_part)
            except StopIteration as e:
                raise get_err(path) from e

    return Path(*correct_parts)
