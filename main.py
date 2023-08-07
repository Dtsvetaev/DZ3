def get_file_content(file_path, encoding='utf-8'):
    with open(file_path, 'r', encoding=encoding) as file:
        content = file.readlines()
    return content


def write_sorted_files(input_files, output_file, encoding='utf-8'):
    file_contents = {}


    for file_name in input_files:
        content = get_file_content(file_name, encoding=encoding)
        file_contents[file_name] = (len(content), content)


    sorted_files = sorted(file_contents.items(), key=lambda x: x[1][0])


    with open(output_file, 'w', encoding=encoding) as output:
        for file_name, (num_lines, content) in sorted_files:
            output.write(f"{file_name}\n{num_lines}\n")
            output.writelines(content)
            output.write('\n')



input_files = ["1.txt", "2.txt"]
output_file = "result.txt"
write_sorted_files(input_files, output_file, encoding='utf-8')
