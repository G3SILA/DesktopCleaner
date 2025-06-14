from pathlib import Path
import config 

# check if desktop exist / valid
def ensure_home():
    if not config.DESKTOP_PATH.exists():
        raise FileNotFoundError(f"Path does not exist: {config.DESKTOP_PATH}")
    if not config.DESKTOP_PATH.is_dir():
        raise NotADirectoryError(f"{config.DESKTOP_PATH} is not a valid directory")

# check folder, create folder if DNE
def ensure_folder(folder_name: str) -> Path:
    FOLDER_PATH = config.DESKTOP_PATH / folder_name
    FOLDER_PATH.mkdir(exist_ok=True)
    return FOLDER_PATH

