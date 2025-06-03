import os

def rename_folders_in_directory(directory_path, old_pattern, new_pattern):
    try:
        # List all items in the desired directory
        items = os.listdir(directory_path)

        # Filter out items that are not directories
        folders = [item for item in items if os.path.isdir(os.path.join(directory_path, item))]

        for folder in folders:
            # Check if the folder name contains the old pattern
            if old_pattern in folder:
                # Create the new folder name by replacing the old pattern with the new pattern
                new_folder_name = folder.replace(old_pattern, new_pattern)
                # Get the full paths for the current and new folder names
                current_path = os.path.join(directory_path, folder)
                new_path = os.path.join(directory_path, new_folder_name)
                # Rename the desired folder
                os.rename(current_path, new_path)
                print(f'Renamed "{current_path}" to "{new_path}"')

        print("Folder renaming completed successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
directory_path = os.getcwd()  # Which dir?
old_pattern = '_2'
new_pattern = '' 

rename_folders_in_directory(directory_path, old_pattern, new_pattern)
