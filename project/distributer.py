import utils
import log

# move files into folders
def organize_desktop():
    log_file = log.get_log_path(utils.DESKTOP_PATH)
    moved_files = []      # pairs in (new, old)
    
    for item in utils.DESKTOP_PATH.iterdir():
        if item.is_file():
            CATEGORY = utils.classify_file(item.name)
            FOLDER = utils.ensure_folder(utils.DESKTOP_PATH, CATEGORY)
            FINAL_PATH = FOLDER / item.name
            try:
                item.rename(FINAL_PATH)   # move
                moved_files.append((str(FINAL_PATH), str(item)))      # log the file, (new, old) 
                print(f"✅ move:{item.name} --> {CATEGORY}/")
            except Exception as e:
                print(f"❌ failed moving:{item.name}, {e}")
                
    log.write_log(moved_files, log_file)
                
