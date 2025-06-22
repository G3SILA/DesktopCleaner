import distributer
import utils
import log


# command for quit
# quit is always the last option
QUIT = '4'

def menu():
    while True:
        print("\n=== Desktop Cleaner Menu ===")
        print("1. Run Cleaner")
        print("2. Restore Last Cleanup")
        print("3. Check Last Log Info (We skip restored log files)")
        print(f"{QUIT}. Quit")

        choice = input(f"Enter (1-{QUIT}): ").strip()
        if choice == '1':
            if not utils.read_path():
                continue
            distributer.organize_desktop()
        elif choice == '2':
            log_file = log.get_latest_log(utils.DESKTOP_PATH)
            log.restore_latest(log_file)
        elif choice == '3':
            if not utils.read_path():
                continue
            log_file = log.get_latest_log(utils.DESKTOP_PATH)
            if (log_file): 
                log.print_log(log_file)
        elif choice == QUIT:
            break
        else:
            print(f"Invalid input. Please enter 1-{QUIT}.")



def main(): 
    menu()
    input("------Done------\nPress Enter to exit...")

main(); 
