from pathlib import Path
from colorama import Fore
import sys

# List of possible directories
FOLDERS = []

def visualize_dir(path: str):
    # Function takes path to the directory and visualize its structure in terminal (Folder - green color, File - blue color)

    for path in path.iterdir():

        if(path.is_dir()):
            num_of_spaces_dir = FOLDERS.index(path.parent.name) + 1

            print(f'{Fore.GREEN}{'    '*num_of_spaces_dir}{path.name}{Fore.RESET}')

            FOLDERS.append(f'{path.name}')

            visualize_dir(path)

        if(path.is_file()):
            num_of_spaces_file = FOLDERS.index(path.parent.name) + 1

            print(f'{Fore.BLUE}{'    '*num_of_spaces_file}{path.name}{Fore.RESET}')
    

def main():
    try:
        path = Path(sys.argv[1])

        # Check if the path is dir
        if(path.is_file()):
            raise ValueError

        # Print name of search dir
        print(f'{Fore.GREEN}{path.name}{Fore.RESET}')

        # Add to the list of possible dir
        FOLDERS.append(f'{path.name}')

        visualize_dir(path)

    except:
        print('Something went wrong. Please check path!')
    

if __name__ == '__main__':
    main()