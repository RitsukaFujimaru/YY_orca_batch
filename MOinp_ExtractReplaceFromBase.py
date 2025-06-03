import os
import re

def extract_and_replace(file_path, extract_patterns):
    """Extract patterns from the file and use them to perform replacements in the file."""
    with open(file_path, 'r', newline='') as file:
        oldlines = file.readlines()

    new_lines = oldlines.copy() # Do not modify the original file
    for extract_pattern in extract_patterns:
        base_pattern = extract_pattern['base_pattern']
        replacements_patterns = extract_pattern['replacements_patterns']
        
        # Find the base pattern and extract the variable part
        extracted_value = None
        for line in oldlines:
            match = re.search(base_pattern, line)
            if match:
                extracted_value = match.group(1) # regex catching the first desired group.
                break

        if extracted_value:
            for i, line in enumerate(new_lines):
                for search_pattern, replace_pattern in replacements_patterns:
                    new_lines[i] = re.sub(search_pattern, replace_pattern.replace("{extracted}", extracted_value), new_lines[i]) # Construct a new string and replace the desired string in oldlines with the created string.

    # Ensure Linux newline
    with open(file_path, 'w', newline='\n') as file:
        for line in new_lines:
            file.write(line.strip('\r\n') + '\n')
    print(f"Processed {file_path}")

def replace_in_inp_files(directory, extract_patterns):
    """Extract patterns and perform replacements in all .inp files in the specified directory and its subdirectories."""
    for root, _, files in os.walk(directory):  # Traverse the directory tree
        for file in files:
            if file.endswith('.inp'):  # Check the .inp extension
                file_path = os.path.join(root, file)  # Full path
                extract_and_replace(file_path, extract_patterns)

if __name__ == "__main__":
    # Directory with the desired .inp files
    directory = os.getcwd()
    
    extract_patterns = [
        {
            'base_pattern': r'%base\s+"LH2_CASSCF_19_14_def2_Pi7_NRoot4_(\w+)"',
            'replacements_patterns': [
                #(r'%moinp\s+"LH2_CASSCF_19_14_def2_Pi7_NRoot1_\w+\.gbw"', '%moinp "LH2_CASSCF_19_14_def2_Pi7_NRoot1_{extracted}.gbw"'),
                #(r'MOinp\s+"LH2_CASSCF_19_14_def2_Pi7_NRoot1_\w+\.gbw"', 'MOinp "LH2_CASSCF_19_14_def2_Pi7_NRoot1_{extracted}.gbw"'),
                (r'%moinp\s+"LH2_CASSCF_19_14_def2_Pi7_NRoot4_\w+\.gbw"', '%moinp "LH2_CASSCF_19_14_def2_Pi7_NRoot4_2p2A_Planar.gbw"'),
                (r'MOinp\s+"LH2_CASSCF_19_14_def2_Pi7_NRoot4_\w+\.gbw"', 'MOinp "LH2_CASSCF_19_14_def2_Pi7_NRoot4_2p2A_Planar.gbw"'),
            ]
        },
    ]
    
    replace_in_inp_files(directory, extract_patterns)
    print("Replacement complete.") 
