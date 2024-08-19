import json

# Load the JSON data from the provided file
file_path = ''
with open(file_path, 'r') as file:
    data = json.load(file)

# Extract all spo_list entries and write them to a new text file
output_file_path = ''
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    for entry in data:
        if 'spo_list' in entry:
            spo_line = ' '.join([str(spo) for spo in entry['spo_list']])
            output_file.write(spo_line + '\n')

