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
                logfile.write(f"{old_path} -> {new_path}\n")
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
# Note: this would skip any (restored) log files
def get_latest_log(work_folder: Path) -> Path:
    log_path = work_folder / "log_info"                       
    logs = sorted(log_path.glob("*.log"), reverse=True)   #descending order
    if not logs: 
        print("No earlier log info found.")
        return None
    return logs[0]


# restore the most recent clean-up 
def restore_latest(log_file: Path):
    if not log_file.exists():
        print(f"Log file not found: {log_file}")
        return
    # restore
    with open(log_file, 'r', encoding='utf-8') as log:
        for line in log: 
            ori_path_str, new_path_str = map(str.strip, line.split("->"))
            ori_path = Path(ori_path_str)
            new_path = Path(new_path_str)
            if new_path.exists() and ori_path.parent.exists():
                new_path.rename(ori_path)
                print(f"Restored: {new_path.name} to {ori_path}")
            else:
                print(f"File not found: {new_path.name}\n"
                      f"OR original folder doesn't exist: {ori_path}")
    # change log file
    newlog_name = f"(restored)_at_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}_original_{log_file.name}"
    path = log_file.parent / newlog_name
    log_file.rename(path)


            
        
