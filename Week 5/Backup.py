import sys
import shutil


def create_backup(filename):
    try:
        if not shutil.os.path.isfile(filename):
            print(f"The file '{filename}' does not exist.")
            return

        backup_filename = filename + ".bak"

        shutil.copyfile(filename, backup_filename)

        print(f"Backup created: '{backup_filename}'")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python create_backup.py <filename>")
    else:
        filename = sys.argv[1]
        create_backup(filename)
