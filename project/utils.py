import pathlib 
import config 

### my test directory as a default
DESKTOP_PATH = pathlib.Path("D:/DesktopCleaner/DesktopCleaner/desktop_test")


## read into DESKTOP_PATH
def read_path():
    global DESKTOP_PATH
    path_str = input("Enter the path you want to work with: ").strip()
    DESKTOP_PATH = pathlib.Path(path_str)
    return ensure_path(DESKTOP_PATH)

# check if path to a directory exist / valid
def ensure_path(path: pathlib.Path) -> bool:
    if not path.exists():
        print(f"Path does not exist: {path}")
        return False
    if not path.is_dir():
        print(f"{path} is not a valid directory")
        return False
    return True


# check folder under given path with name folder_name, create folder if DNE
def ensure_folder(path: pathlib.Path, folder_name: str) -> pathlib.Path:
    FOLDER_PATH = path / folder_name
    FOLDER_PATH.mkdir(exist_ok=True)
    return FOLDER_PATH


# return the setted file type of a file 
def classify_file(filename: str) -> str:
    filetype = filename.lower().split('.')[-1]
    filetype = '.' + filetype if '.' in filename else ''

    for category, extensions in config.CATEGORIES.items():
        if filetype in extensions:
            return category
    return "OTHER"
