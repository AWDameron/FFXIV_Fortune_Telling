import Fortune_Lists
import random
import os
import tkinter as tk
from Fortune_Teller_Method import fortune_telling_random
from Dialog_Box import *


def main():
    # Get the current working directory
    current_directory = os.getcwd()
    
    # Create the absolute file path
    file_path = os.path.join(current_directory, "Fortunes_told.txt")
    
    # Create the file if it doesn't exist
    if not os.path.isfile(file_path):
        with open(file_path, "w") as file:
            # Just create an empty file; you could also write a header or initial content if desired
            pass
        print(f"Created file: {file_path}")
    else:
        print(f"File already exists: {file_path}")
    
    dialog_box(file_path)
    return

if __name__ == "__main__":
    main()