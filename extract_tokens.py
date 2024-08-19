import json

# Load the JSON file
file_path = ''
with open(file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

# Extract tokens
tokens_list = [sample['tokens'] for sample in data]

# Save to a txt file
output_file_path = ''
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    for tokens in tokens_list:
        output_file.write(tokens + '\n')


