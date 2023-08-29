def find_file_differences(file1, file2):
    iccids1 = set()
    iccids2 = set()

    with open(file1, 'r') as f1:
        for line in f1:
            iccid = line.strip()
            iccids1.add(iccid)

    with open(file2, 'r') as f2:
        for line in f2:
            iccid = line.strip()
            iccids2.add(iccid)

    differences = iccids1.difference(iccids2)
    return differences

# Example usage
file1_path = 'C:\\Users\\renzz\\Documents\\RENZZO\\TEXT\\Set1.txt'
file2_path = 'C:\\Users\\renzz\\Documents\\RENZZO\\TEXT\\Set2.txt'

differences = find_file_differences(file1_path, file2_path)
print("ICCID(s) present in file1 but not in file2:")
for diff in differences:
    print(diff)

differences = find_file_differences(file2_path, file1_path)
print("ICCID(s) present in file2 but not in file1:")
for diff in differences:
    print(diff)
