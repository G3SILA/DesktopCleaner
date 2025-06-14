import pathlib

CATEGORIES = {
    "PICTURE": [".jpg", ".jpeg", ".png"],
    "DOCUMENT": [".pdf", ".docx", ".txt"],
    "VIDEO": [".mp4", ".avi"],
    "OTHER": []
}


### my test directory as a default
DESKTOP_PATH = pathlib.Path("D:/DesktopCleaner/DesktopCleaner/desktop_test")


def read_path():
    global DESKTOP_PATH
    path_str = input("Enter the path you want to work with: ").strip()
    DESKTOP_PATH = pathlib.Path(path_str)
    ensure_home()

# check if desktop exist / valid
def ensure_home():
    if not DESKTOP_PATH.exists():
        raise FileNotFoundError(f"Path does not exist: {DESKTOP_PATH}")
    if not DESKTOP_PATH.is_dir():
        raise NotADirectoryError(f"{DESKTOP_PATH} is not a valid directory")


