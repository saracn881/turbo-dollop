def split_file(file_path, num_parts):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    total_lines = len(lines)
    lines_per_part = total_lines // num_parts

    for i in range(num_parts):
        start = i * lines_per_part
        end = start + lines_per_part if i < num_parts - 1 else None
        part_lines = lines[start:end]

        part_file_path = f'part_{i+1}.txt'
        with open(part_file_path, 'w') as part_file:
            part_file.writelines(part_lines)

        print(f'Part {i+1} saved to {part_file_path}.')

# Example usage:
file_path = r'C:\Users\oluwa\OneDrive\Documents\my files\1.txt'
num_parts = 10
split_file(file_path, num_parts)
