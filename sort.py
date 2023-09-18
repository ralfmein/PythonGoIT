import shutil
from pathlib import Path


def normalize(name):
    name = ''.join(c if c.isalnum() or c == '.' else '_' for c in name)
    return name


def organize_files(folder):
    for item in folder.iterdir():
        if item.is_dir():
            organize_files(item)
        else:
            file_extension = item.suffix.lower()
            destination_folder = None

            if file_extension in ('.jpeg', '.png', '.jpg', '.svg'):
                destination_folder = 'images'
            elif file_extension in ('.avi', '.mp4', '.mov', '.mkv'):
                destination_folder = 'video'
            elif file_extension in ('.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx'):
                destination_folder = 'documents'
            elif file_extension in ('.mp3', '.ogg', '.wav', '.amr'):
                destination_folder = 'audio'
            elif file_extension in ('.zip', '.gz', '.tar'):
                destination_folder = 'archives'

            if destination_folder:
                dest_dir = folder / destination_folder
                dest_dir.mkdir(parents=True, exist_ok=True)
                new_name = normalize(item.stem) + item.suffix
                new_path = dest_dir / new_name
                shutil.move(item, new_path)
            else:
                new_name = normalize(item.name)
                new_path = folder / new_name
                item.rename(new_path)


def main(source_folder):
    source_path = Path(source_folder)
    if source_path.is_dir():
        organize_files(source_path)
        print("Сортування завершено.")
    else:
        print("Зазначений шлях не вказує на директорію.")


if __name__ == "__main__":
    import sys

    source_folder = sys.argv[1]
    main(source_folder)
