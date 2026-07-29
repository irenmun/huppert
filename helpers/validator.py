from pathlib import Path


def validate_directory(path: str):
    directory = Path(path)

    if not directory.exists():
        raise FileNotFoundError(path)

    if not directory.is_dir():
        raise NotADirectoryError(path)

    return directory
