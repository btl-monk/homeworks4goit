print("_____________________________task03________________________________________________________________")

import sys
from pathlib import Path
from colorama import Fore

def show_me_your_dir(some_path, indent=0):
    my_path = Path(some_path)
    # check if the path from the user is correct
    if not my_path.exists or not my_path.is_dir:
        print(f"Houston, we have a problem! {some_path} not exist or {some_path} not a dir!")
        return
    # using colorama and some indents for better look
    for item in my_path.iterdir():
        if item.is_dir():
            print(" " * indent + Fore.GREEN + f"Directory: {str(item)}")
            show_me_your_dir(item, indent+5)
        elif item.is_file():
            print(" " * indent + Fore.BLUE + f"File: {str(item)}")
            
if __name__ == "__main__":
    # checking if user enter path to directory
    if len(sys.argv) != 2:
        print("Please, enter path to directory.")
        sys.exit(1)

    directory_path = sys.argv[1]
    show_me_your_dir(directory_path)

