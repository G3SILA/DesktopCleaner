import utils
from pathlib import Path
from datetime import datetime

# return the current file_path for next log  
def get_log_path(parent_path : Path) -> Path: 
    log_folder = utils.ensure_folder(parent_path, "log_info")
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    return log_folder / f"{timestamp}.log"

# write into log_file from moved_files
def write_log(moved_files: list[tuple[str, str]], log_file: Path):
    try:
        with open(log_file, 'w', encoding='utf-8') as logfile:
            for new_path, old_path in moved_files:
                logfile.write(f"{new_path} -> {old_path}\n")
        print(f"New log saved as {log_file.name}")
    except Exception as e:
        print(f"Failed to write log file: {e}")
        
# print the given log_path
def print_log(log_path: Path):
    try:
        print(f"Log file: {log_path.name}")
        print("Moved files:\n")

        with open(log_path, 'r', encoding='utf-8') as log:
            for line in log:
                print("  " + line)
    except Exception as e:
        print(f"Failed to read log: {e}")

# return the path of the lastest log file 
def get_latest_log(work_folder: Path) -> Path:
    log_path = work_folder / "log_info"                       
    logs = sorted(log_path.glob("*.log"), reverse=True)   #descending order
    if not logs: 
        print("No earlier log info found.")
        return None
    return logs[0]


