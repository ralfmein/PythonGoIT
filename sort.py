import shutil
from pathlib import Path


def normalize(name):
    normalized_name = ""
    for char in name:
        if char.isalnum():
            normalized_name += char
        elif char.isspace() or char == '.':
            normalized_name += "_"
        elif char.isalpha():
            normalized_name += char.encode('ascii', 'ignore').decode()
        else:
            normalized_name += "_"
    return normalized_name


def unpack_archive(archive_path, destination_folder):
    shutil.unpack_archive(archive_path, destination_folder)


def organize_files(source_folder, root_folder):

    categories = {
        'images': ('.jpeg', '.png', '.jpg', '.svg'),
        'video': ('.avi', '.mp4', '.mov', '.mkv'),
        'documents': ('.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx'),
        'audio': ('.mp3', '.ogg', '.wav', '.amr'),
        'archives': ('.zip', '.gz', '.tar')
    }

    for item in source_folder.iterdir():
        if item.is_dir():
            organize_files(item, root_folder)
        else:
            file_extension = item.suffix.lower()
            destination_folder = None

            for category, extensions in categories.items():
                if file_extension in extensions:
                    destination_folder = category
                    break

            if destination_folder:
                dest_dir = root_folder / destination_folder
                dest_dir.mkdir(parents=True, exist_ok=True)

                new_name = normalize(item.stem) + item.suffix
                new_path = dest_dir / new_name
                if destination_folder == 'archives':
                    unpack_archive(item, new_path)
                else:
                    shutil.move(item, new_path)


def main():
    if len(sys.argv) != 2:
        print("Usage: python sort.py source_folder")
        return

    source_folder = Path(sys.argv[1])

    if not source_folder.is_dir():
        print("The specified path does not point to a directory.")
        return

    organize_files(source_folder, source_folder)


if __name__ == "__main__":
    import sys
    main()
