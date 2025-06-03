import os
import re

def modify_inp_files(root_directory):
    for subdir, _, files in os.walk(root_directory):
        for file in files:
            if file.endswith(".inp"):
                file_path = os.path.join(subdir, file)
                with open(file_path, 'r') as inp_file:
                    content = inp_file.read()

                # Normalize to Linux newline
                content = content.replace('\r\n', '\n').replace('\r', '\n')

                # Pattern extraction in content and replacement
                content = re.sub(r'(%moinp\s+"LH2_CASSCF_19_14_def2_Pi7_)NRoot1(_[^"]*\.gbw")', r'\1NRoot5\2', content)
                content = re.sub(r'(MOinp\s+"LH2_CASSCF_19_14_def2_Pi7_)NRoot1(_[^"]*\.gbw")', r'\1NRoot5\2', content)

                # Ensure Linux newline
                with open(file_path, 'w', newline='\n') as inp_file:
                    inp_file.write(content)

                # Print processed
                print(f"Processed file: {file_path}")

if __name__ == "__main__":
    root_dir = os.getcwd()
    modify_inp_files(root_dir)
