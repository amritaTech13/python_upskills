import os
import glob

directory_path = os.path.join('Task1','dir1','dir2')
all_py_file = glob.glob(os.path.join(directory_path, "*.py"))

print(all_py_file)

for file in all_py_file:
    with open(file, 'r') as f:
        line_count = sum(1 for each_line in f )
    print(f"File: {file} \nLine Count: { line_count}")   