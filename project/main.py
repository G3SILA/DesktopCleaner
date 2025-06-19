import distributer
import utils

# command for quit
# quit is always the last option
QUIT = '3'

def menu():
    while True:
        print("\n=== Desktop Cleaner Menu ===")
        print("1. Run Cleaner")
        print("2. Restore Last Cleanup")
        print(f"{QUIT}. Quit")

        choice = input(f"Enter (1-{QUIT}): ").strip()
        if choice == '1':
            if not utils.read_path():
                continue
            distributer.organize_desktop()
        elif choice == '2':
            print("Restoring last cleanup...")
            ####
        elif choice == QUIT:
            break
        else:
            print(f"Invalid input. Please enter 1-{QUIT}.")



def main(): 
    menu()
    input("------Done------\nPress Enter to exit...")

main(); 
