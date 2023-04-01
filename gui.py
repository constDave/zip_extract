import PySimpleGUI as sg
from zip_extract import extract_archive
sg.theme("DarkTeal2")

label1 = sg.Text("Select archive: ")
input1 = sg.Input()
choose_button1 = sg.FileBrowse("Choose", key="archive")

label2 = sg.Text("Select dest dir: ")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key="folder")

extract_button = sg.Button("Extract")
output_label = sg.Text(key="output", text_color="green")

exit_button = sg.Button("Exit")


window = sg.Window("Archive Extractor", layout=[
    [label1, input1, choose_button1],
    [label2, input2, choose_button2],
    [extract_button, output_label, exit_button]

])

while True:
    event, values = window.read()
    if event == "Exit":
        break

    archive_path = values["archive"]
    dest_path = values["folder"]
    extract_archive(archive_path=archive_path, dest_folder=dest_path)
    window["output"].update(value="Extract successful.")


window.close()
