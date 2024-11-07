import tkinter as tk
from tkinter import filedialog
from pathlib import Path
import os


def timer(fn):
    from time import perf_counter

    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = fn(*args, **kwargs)
        stop = perf_counter()
        print(f'Function {fn.__name__} took {stop - start:0.4f} seconds')
        return result
    return wrapper


def select_excel_file():
    """
    This function opens a file dialog to select an Excel file (.xlsx or .xls).
    If the file is invalid or no file is selected, the user will be prompted
    to continue or end the process.
    """
    # Initialize Tkinter root (it won't display a window itself)
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Define the initial directory as the Desktop
    initial_directory = Path(os.path.expanduser("~/Desktop"))

    # While loop to repeatedly prompt the user until a valid Excel file is selected
    while True:
        # Show a file dialog to select the Excel file, starting from the Desktop
        file_path = filedialog.askopenfilename(
            title="Select the Excel file to be validated",
            initialdir=initial_directory,  # Set the starting directory to Desktop
            filetypes=[("Excel files", "*.xlsx *.xls")]
        )

        # Validate if a file was selected and if it's an Excel file
        if file_path:
            file_path = Path(file_path)

            # Check if the file has the correct Excel extension
            if file_path.suffix.lower() in ['.xlsx', '.xls']:
                return file_path  # Return the valid file path and exit the function
            else:
                print("The selected file is not an Excel file.")
        else:
            print("No file selected.")

        # Ask the user if they want to continue or end the process if the file is invalid or not selected
        continue_choice = input("Do you want to continue? (yes/no): ").strip().lower()
        if continue_choice != 'yes':
            print("Process ended.")
            break  # Exit the loop if the user chooses 'no'

    # Destroy the Tkinter root instance
    root.destroy()



