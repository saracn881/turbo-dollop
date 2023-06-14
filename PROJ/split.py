def split_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    num_lines = len(lines)
    num_parts = (num_lines // 10000) + 1

    for i in range(num_parts):
        start = i * 10000
        end = start + 10000
        part_lines = lines[start:end]

        part_file_name = f'part_{i+1}.txt'
        with open(part_file_name, 'w') as part_file:
            part_file.writelines(part_lines)

        print(f'Successfully created {part_file_name}')

# Usage example
file_path = r'C:\Users\oluwa\OneDrive\Documents\my files\compilation\main comp.txt'
split_file(file_path)
