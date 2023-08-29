import os
import csv

file_path = 'C:\\Users\\renzz\\Documents\\RENZZO\\LINKS FIELD\\PYTHON SCRIPTS\\setelht.txt'

def convert_file_to_list(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()

    numbers = []
    for line in lines:
        numbers.extend(line.split())

    numbers = [int(number) for number in numbers]

    return numbers

def export_to_csv(data_list, filename):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(data_list)

if __name__ == "__main__":
    numbers = convert_file_to_list(file_path)

    output_directory = 'C:\\Users\\renzz\\Documents\\RENZZO\\LINKS FIELD\\PYTHON SCRIPTS\\'
    csv_filename = os.path.join(output_directory, 'output.csv')
    export_to_csv(numbers, csv_filename)
    print(f"Data exported to {csv_filename} successfully.")
