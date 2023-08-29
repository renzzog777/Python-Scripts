import os

script_directory = os.path.dirname(os.path.abspath(__file__))
output_file = os.path.join(script_directory, 'output_items.txt')

file_path = 'C:\\Users\\renzz\\Documents\\RENZZO\\LINKS FIELD\\PYTHON SCRIPTS\\countries.txt'

with open(file_path, 'r') as file:
    contents = file.read()

items = contents.split(';')

with open(output_file, 'w') as output:
    for item in items:
        output.write(item + '\n')

print(f"Items exported to {output_file}")