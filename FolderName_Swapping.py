import os

def rename_folders(base_path):
    # Get a list of all primary folders in the desired directory
    folders = [f for f in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, f))]

    for folder in folders:
        # Split the folder name by '_'
        parts = folder.split('_')
        if len(parts) == 2:
            # Swapping!
            new_folder_name = f"{parts[1]}_{parts[0]}"
            old_path = os.path.join(base_path, folder)
            new_path = os.path.join(base_path, new_folder_name)

            # Renaming!
            os.rename(old_path, new_path)
            print(f"Renamed '{folder}' to '{new_folder_name}'")

# Specify the directory to process
base_path = os.getcwd()  # Use the current directory as the root folder

# Run the renaming function
rename_folders(base_path)
