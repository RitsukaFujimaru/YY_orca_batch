import os

def delete_files(root_dir, file_extensions):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for file in filenames:
            if any(file.endswith(ext) for ext in file_extensions):
                file_path = os.path.join(dirpath, file)
                try:
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")
                except Exception as e:
                    print(f"Error deleting {file_path}: {e}")

if __name__ == "__main__":
    # Define the root directory
    root_directory = os.getcwd()

    # The file extensions you want to delete
    file_extensions = ['.densities', '.tmp', 'property.txt', '.error', '.out', '.nodelist']

    delete_files(root_directory, file_extensions)

