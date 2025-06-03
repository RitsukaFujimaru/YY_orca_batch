import os

def delete_unmatched_gbw_files(root_dir):
    for subdir, _, files in os.walk(root_dir):
        subdir_name = os.path.basename(subdir)
        for file in files:
            if file.endswith('.gbw'):
                if subdir_name not in file:
                    file_path = os.path.join(subdir, file)
                    print(f'Deleting {file_path}')
                    os.remove(file_path)

if __name__ == "__main__":
    root_directory = os.getcwd()
    delete_unmatched_gbw_files(root_directory)
