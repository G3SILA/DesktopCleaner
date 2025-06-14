import config
import directory


def classify_file(filename: str) -> str:
    filetype = filename.lower().split('.')[-1]
    filetype = '.' + filetype if '.' in filename else ''

    for category, extensions in config.CATEGORIES.items():
        if filetype in extensions:
            return category
    return "OTHER"


def organize_desktop():
    for item in config.DESKTOP_PATH.iterdir():
        if item.is_file():
            CATEGORY = classify_file(item.name)
            FOLDER = directory.ensure_folder(CATEGORY)
            FINAL_PATH = FOLDER / item.name
            try:
                item.rename(FINAL_PATH)                   # move
                print(f"✅ move:{item.name} --> {CATEGORY}/")
            except Exception as e:
                print(f"❌ failed moving:{item.name}, {e}")
