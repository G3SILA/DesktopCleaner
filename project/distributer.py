import utils

# move files into folders
def organize_desktop():
    for item in utils.DESKTOP_PATH.iterdir():
        if item.is_file():
            CATEGORY = utils.classify_file(item.name)
            FOLDER = utils.ensure_folder(utils.DESKTOP_PATH, CATEGORY)
            FINAL_PATH = FOLDER / item.name
            try:
                item.rename(FINAL_PATH)   # move
                print(f"✅ move:{item.name} --> {CATEGORY}/")
            except Exception as e:
                print(f"❌ failed moving:{item.name}, {e}")
                
