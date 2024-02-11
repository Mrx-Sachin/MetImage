# Metimage

Metimage is a Python-based program designed to remove EXIF or metadata from images while preserving image quality. It provides a convenient way to process individual images or entire folders, making it easy to manage metadata removal at scale.

## Features

- Removes EXIF and other metadata from images.
- Preserves image quality during the process.
- Supports processing of individual images or entire folders.
- Simple and easy-to-use Graphical-user interface.

## Requirements

- Python 3.x
- Pillow library (Python Imaging Library)
- tkinter

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Mrx-Sachin/MetImage.git
    ```

2. Navigate to the project directory:

    ```bash
    cd MetImage
    ```

3. run the MetImage Python file:

    ```bash
    python -u metimage.py
    ```

## Usage

### GUI Usage

1. Run the `metimage.py` file to launch the GUI application.

2. The main window will display with the options to select a file or a folder.

3. To remove metadata from a single image:
    - Click on the "Select File" button.
    - Choose the image file(s) you want to process.
    - A new window will prompt you to select the save option:
        - Click on "Same Directory" to save the modified images in the same directory as the original image(s).
        - Click on "Different Directory" to choose a different directory to save the modified images.
        - Click on "Cancel" to cancel the operation.

4. To remove metadata from images in a folder:
    - Click on the "Select Folder" button.
    - Choose the folder containing the image files you want to process.
    - A new window will prompt you to select the save option:
        - Click on "Same Directory" to save the modified images in the same directory as the original images.
        - Click on "Different Directory" to choose a different directory to save the modified images.
        - Click on "Cancel" to cancel the operation.

5. Once you've selected the save option, the program will process the images, remove metadata, and save the modified images accordingly.


