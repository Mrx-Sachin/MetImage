
import tkinter as tk
from tkinter import filedialog
from PIL import Image
import os
import re

def save_image_with_mod(image_path, save_folder):
    # Read the image
    image = Image.open(image_path)
    file_name = os.path.basename(image_path)
    file_name, file_extension = os.path.splitext(file_name)
    modified_file_name = file_name + "_mod" + file_extension
    print("modefyed file  ",modified_file_name)
    image.save(os.path.join(save_folder, modified_file_name))


def select_save_file(file_paths):
    # Ask user to select a folder to save the modified images
    save_folder = filedialog.askdirectory()
    try:
        # Save the modified images in the selected folder
        for file_path in file_paths:
            print("file path ",file_path)
            print("save folder ",save_folder)
            save_image_with_mod(file_path, save_folder)
    except Exception as e:  # Catch any exception that occurs
        print(f"An error occurred: {e}")
    
def save_fimages(file_paths):
    # Process each image file in the selected folder
    try:
        # Save the modified images in the selected folder
        for file_path in file_paths:
            save_folder = re.search(r'(.+)/[^/]+$', file_path).group(1)
            print("save folder ",save_folder) 
            print("folder path ",file_path)
            save_image_with_mod(file_path, save_folder)
    except Exception as e:  # Catch any exception that occurs
        print(f"An error occurred: {e}")

def select_save_folder(folder_path):
    # Ask user to select a different folder to save the modified images
    save_folder = filedialog.askdirectory()
    try:
        # Save the modified images in the selected folder
        # save_images(folder_path, save_folder)
        for file_name in os.listdir(folder_path):
            if file_name.endswith('.jpg') or file_name.endswith('.png'):
                file_path = os.path.join(folder_path, file_name)
                save_image_with_mod(file_path, save_folder)
                print(f"Processed: {file_name}")
    except Exception as e:  # Catch any exception that occurs
        print(f"An error occurred: {e}")

def save_images(folder_path, save_folder):
    # Process each image file in the selected folder
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.jpg') or file_name.endswith('.png'):
            file_path = os.path.join(folder_path, file_name)
            save_image_with_mod(file_path, save_folder)
            print(f"Processed: {file_name}")
    

def select_folder():
    # Create a file dialog to select a folder containing image files
    folder_path = filedialog.askdirectory()
    print(folder_path)
    save_option_window = tk.Toplevel()
    save_option_window.title("Save Option")

    # Add a label with save option prompt
    save_option_label = tk.Label(save_option_window, text="Do you want to save the modified images in the same directory?")
    save_option_label.pack(pady=10)

    # Create the buttons for save options
    same_directory_button = tk.Button(save_option_window, text="Same Directory", command=lambda: save_images(folder_path, folder_path))
    different_directory_button = tk.Button(save_option_window, text="Different Directory", command=lambda: select_save_folder(folder_path))
    cancel_button = tk.Button(save_option_window, text="Cancel", command=save_option_window.destroy)

    # Add the buttons to the save option window
    same_directory_button.pack(pady=10)
    different_directory_button.pack(pady=10)
    cancel_button.pack(pady=10)

    # Wait for the save option window to close before continuing
    save_option_window.wait_window(save_option_window)

def select_file():
    # Create a file dialog to select one or more image files
    file_paths = filedialog.askopenfilenames()
    print(file_paths)
    ## Ask user to select a folder to save the modified images
    save_option_window = tk.Toplevel()
    save_option_window.title("Save Option")

    # Add a label with save option prompt
    save_option_label = tk.Label(save_option_window, text="Do you want to save the modified images in the same directory?")
    save_option_label.pack(pady=10)

    # Create the buttons for save options
    same_directory_button = tk.Button(save_option_window, text="Same Directory", command=lambda: save_fimages(file_paths))
    different_directory_button = tk.Button(save_option_window, text="Different Directory", command=lambda: select_save_file(file_paths))
    cancel_button = tk.Button(save_option_window, text="Cancel", command=save_option_window.destroy)

    # Add the buttons to the save option window
    same_directory_button.pack(pady=10)
    different_directory_button.pack(pady=10)
    cancel_button.pack(pady=10)

    # Wait for the save option window to close before continuing
    save_option_window.wait_window()


# Create the main window
window = tk.Tk()

# Set the initial window size
window.geometry("400x200")
window.title("Metimage")
# Add a label with text
label = tk.Label(window, text="Select an option:")
label.pack(pady=10)

# Create the buttons
file_button = tk.Button(window, text="Select File", command=select_file)
folder_button = tk.Button(window, text="Select Folder", command=select_folder)
cancel_button = tk.Button(window, text="Cancel", command=window.destroy)

# Add the buttons to the window
file_button.pack(pady=10)
folder_button.pack(pady=10)
cancel_button.pack(pady=10)

# Start the main loop
window.mainloop()

