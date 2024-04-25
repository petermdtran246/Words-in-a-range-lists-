# Read input file name and search range
file_name = input().strip()
lower_bound = input().strip()
upper_bound = input().strip()

# Open file and read the lines
with open(file_name, 'r') as file:
    lines = file.readlines()

# Check if strings are in the search range
for line in lines:
    word = line.strip()
    if lower_bound <= word <= upper_bound:
        print(word, '- in range')
    else:
        print(word, '- not in range')
