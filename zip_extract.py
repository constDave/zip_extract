import zipfile


def extract_archive(archive_path, dest_folder):
    with zipfile.ZipFile(archive_path, "r") as archive:
        archive.extractall(dest_folder)
