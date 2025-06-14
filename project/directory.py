from pathlib import Path
import config 


# check folder, create folder if DNE
def ensure_folder(folder_name: str) -> Path:
    FOLDER_PATH = config.DESKTOP_PATH / folder_name
    FOLDER_PATH.mkdir(exist_ok=True)
    return FOLDER_PATH

