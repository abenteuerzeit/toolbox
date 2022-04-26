def remove_html_tag_attributes(file, attributes_list, tag):
    # Remove selected attributes from the HTML tag
    # Write True for tag to remove attributes from all tags
    # A new file is generated
    updated_list = [' ' + attribute.lower() + '="' for attribute in attributes_list]
    with open(file) as html_file:
        new_lines = []
        for line in html_file.readlines():
            for attribute in updated_list:
                is_tag = line.strip()
                if is_tag != '':
                    tag_idx = line.find(tag)
                    is_tag = f"<{line[tag_idx]}" in is_tag[0:]
                while is_tag and attribute in line.lower():
                    start = line.find(attribute)
                    if line.find(';'):
                        stop = line.find(';') + 1
                    new_line = line[start:].replace(attribute, "")
                    if new_line.find('"'):
                        stop = new_line.find('"') + 1
                    line = line.replace(new_line[:stop], "")
                    line = line.replace(attribute, "")
            new_lines.append(line)

        file_name = file[:file.find('.html')]
        capitalize = [attribute.upper()[0] + attribute.lower()[1:] for attribute in attributes_list]
        tag = tag if type(tag) is str else "all"
        renamed_file = file_name + f"_{'-'.join(capitalize)}" + f"-removed-from-{tag}" + ".html"
        save_new_file = open(renamed_file, 'w')
        save_new_file.writelines(new_lines)


def remove_tag(file, tag):
    # remove a complete tag from file
    with open(file) as html_file:
        lines = []
        for line in html_file.readlines():
            while tag in line.lower():
                start = line.find(tag)-1
                if line.find('>'):
                    stop = line.find('>') + 1
                new_line = line[start:].replace(tag, "")
                line = line.replace(new_line[:stop], "")
                line = line.replace(tag, "")
        lines.append(line)
        for line in lines:
            print(line)


if __name__ == "__main__":
    # files = [
    #         'add-answer.html',
    #         'add-question.html',
    #         'edit-question.html',
    #         'error.html',
    #         'layout.html',
    #         'question.html'
    #          ]
    # for file in files:
    #     filepath = f"./templates/{file}"
    #     remove_html_tag_attributes(filepath, ["style", "class"])
    # remove_tag('add-question.html', 'a')
    pass
