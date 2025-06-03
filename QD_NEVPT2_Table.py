import os
import re

def find_nevpt2_results(root_folder):
    results = []
    title_line = ["Folder/Filename"]

    for subdir, _, files in os.walk(root_folder):
        for file in files:
            if file.endswith('.log'):
                filepath = os.path.join(subdir, file)
                relative_path = os.path.relpath(filepath, root_folder)
                with open(filepath, 'r') as f:
                    lines = f.readlines()
                
                nevpt2_found = False
                energy_values = []

                for line in lines:
                    if "QD-NEVPT2 Results" in line:
                        nevpt2_found = True
                    if nevpt2_found:
                        match = re.search(r'\s+Total Energy \(E0\+dE\)\s+: E\s+=\s+(-?\d+\.\d+)', line)
                        if match:
                            energy_values.append(match.group(1))
                
                if energy_values:
                    results.append([relative_path] + energy_values)
                    # Ensure the title line has enough columns
                    while len(title_line) < len(energy_values) + 1:
                        title_line.append(f"Root{len(title_line)}")

    return title_line, results

def write_summary_file(title_line, results, output_filename):
    with open(output_filename, 'w', newline='\n') as f:
        f.write('\t'.join(title_line) + '\n')
        for result in results:
            f.write('\t'.join(result) + '\n')

def main():
    root_folder = os.getcwd()  # Use the current directory as the root folder
    output_filename = 'summary.txt'
    title_line, results = find_nevpt2_results(root_folder)
    write_summary_file(title_line, results, output_filename)
    print(f"Summary file '{output_filename}' is done!")

if __name__ == "__main__":
    main()
