# zip_extract
A simple zip file extractor to practice Python with PySimpleGUI

Archive Extractor is a simple Python application that allows you to extract the contents of a ZIP archive to a specified destination folder. The application uses the PySimpleGUI library to create an easy-to-use graphical user interface.

### Dependencies
To use this application, you need to have Python installed along with the following libraries:

### PySimpleGUI
zipfile (part of the Python standard library)
You can install PySimpleGUI using pip:


`pip install PySimpleGUI`

### Usage
Run the Python script:

`python archive_extractor.py`

The Archive Extractor window will appear. Click the "Choose" button next to "Select archive" and browse to the location of the ZIP file you want to extract.

Click the "Choose" button next to "Select dest dir" and browse to the location where you want to extract the contents of the archive.

Click the "Extract" button to start the extraction process. Once the extraction is complete, a message "Extract successful" will appear.

To exit the application, click the "Exit" button.

### Code Structure
The application consists of two main parts:

A graphical user interface (GUI) created using PySimpleGUI.
The extract_archive function, which takes an archive path and a destination folder as arguments and uses the zipfile module to extract the contents of the archive to the specified folder.
The GUI part of the code creates a simple window layout with input fields for selecting the archive and destination folder, as well as buttons for browsing, extraction, and exiting the application. The main loop waits for events such as button clicks and updates the output label to display the extraction status.

The *extract_archive* function uses a context manager to open the provided archive and calls the *extractall* method to extract its contents to the destination folder.