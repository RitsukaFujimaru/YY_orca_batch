import os
import re

def replace_patterns_in_file(file_path, subdir_name, replacements):
    '''Replace specified patterns in the given file with the corresponding subdirectory name.'''
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    for pattern, replacement in replacements.items():
        content = re.sub(pattern, replacement.format(subdir=subdir_name), content)
    
    # Example: Adding content after a specific keyword
    #content = re.sub(r'(%chk\s+"[^"]+")', r'\1\n%mem=4GB', content)  # Adds %mem=4GB after %chk "..."
    
    # Example: Removing a specific line that starts with %oldkeyword
    #content = re.sub(r'^%oldkeyword.*\n', '', content, flags=re.MULTILINE)
    
    # Ensure Linux-style newlines
    content = content.replace('\r\n', '\n')
    
    with open(file_path, 'w', encoding='utf-8', newline='\n') as file:
        file.write(content)

def process_inp_files(base_dir, replacements):
    '''
    Process all .inp files in subdirectories (depth=1) of the given base directory.
    '''
    for subdir in next(os.walk(base_dir))[1]:  # Get subdirectories
        subdir_path = os.path.join(base_dir, subdir)
        for file in os.listdir(subdir_path):
            if file.endswith('.inp'):
                file_path = os.path.join(subdir_path, file)
                replace_patterns_in_file(file_path, subdir, replacements)

if __name__ == '__main__':
    base_directory = './'  # Use current working directory
    
    # Define patterns and their replacements (dynamically using subdir name)
    replacements = {
        #r'%moinp\s+"[^"]+\.gbw"': '%moinp "{subdir}.gbw"',
        #r'%base\s+"[^"]+_FOD"': '%base "{subdir}_FOD"'
    }
    
    process_inp_files(base_directory, replacements)
    print("Replacement complete.")
