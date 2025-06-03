import os
import shutil

def copy_files_to_subdirs(files):
    cwd = os.getcwd()
    subdirs = [d for d in os.listdir(cwd) if os.path.isdir(os.path.join(cwd, d))]
    
    for subdir in subdirs:
        subdir_path = os.path.join(cwd, subdir)
        for file in files:
            if os.path.exists(file):
                shutil.copy(file, subdir_path)
                print(f"Copied {file} to {subdir_path}")
            else:
                print(f"File not found: {file}")

if __name__ == "__main__":
    files = ["LH2CH3_SP_FOD.inp"]  # Specify desired files here, seperate with comma.
    copy_files_to_subdirs(files)
