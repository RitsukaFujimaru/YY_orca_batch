import os

def replace_in_file(file_path, replacements):
    """Replace multiple search_text with replace_text in the desired file."""
    with open(file_path, 'r', newline='') as file:
        oldlines = file.readlines()

    new_lines = []
    for line in oldlines:
        for search_text, replace_text in replacements:
            line = line.replace(search_text, replace_text)  # Replace
        new_lines.append(line.strip('\r\n') + '\n')  # Forcing Linux newline.

    # Write the lines back with Linux newline characters
    with open(file_path, 'w', newline='\n') as file:
        file.writelines(new_lines)  # Write the new contents back to the file

def replace_in_inp_files(directory, replacements):
    """Replace multiple search_text with replace_text in all .inp files in the specified directory and its subdirectories."""
    for root, _, files in os.walk(directory):  # Traverse the directory tree
        for file in files:
            if file.endswith('.inp'):
                file_path = os.path.join(root, file)  # Get the full path of the file
                replace_in_file(file_path, replacements)  # Replace
                print(f"Processed {file_path}")  # Print the file path in console

if __name__ == "__main__":
    # Directory with the *.inp files
    directory = os.getcwd()  # Use the current directory as the root
    
    # List of (search_text, replace_text) tuples
    replacements = [
        #('%Maxcore 7000', '%Maxcore 8400'),
        #('%PAL NProcs 48 END', '%PAL NProcs 40 END'),
        #('%base "LH2_CASSCF_19_14_def2_Pi7_NRoot4', '%base "LH2_CASSCF_19_14_def2_Pi7_NRoot5'),
        #('MOinp "LH2_CASSCF_19_14_def2_Pi7_NRoot4', 'MOinp "LH2_CASSCF_19_14_def2_Pi7_NRoot2'),
        #('%moinp "LH2_CASSCF_19_14_def2_Pi7_NRoot4', '%moinp "LH2_CASSCF_19_14_def2_Pi7_NRoot2'),
        #('NRoots 4', 'NRoots 5'),
        #('Weights[0] = 1,1,1,1 ', 'Weights[0] = 1,1,1,1,1 '),
        #('SwitchStep SuperCI', 'SwitchStep KDIIS'),
        #('OrbStep SuperCI', 'OrbStep KDIIS'),
        #('MO("129.cube",128,0);', ''),
        #('MO("130.cube",129,0);', ''),
        #('MO("131.cube",130,0);', ''),
        #('MO("132.cube",131,0);', ''),
        ('Mult 3', 'Mult 1'),
    ]
    
    replace_in_inp_files(directory, replacements)
    print("Replacement complete.")  
