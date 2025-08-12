#!/usr/bin/python3
'''Markdown to HTML converter script'''


import sys
import os


def line_parse(input_file):
    '''Parse lines inside the README.md (input_file)'''
    lines_list = []
    with open(input_file, "r", encoding='utf-8') as file:
        for line in file:
            line = line.rstrip("\n")
            lines_list.append(line)
    return lines_list


def convert_md_to_html(input_file):
    '''Convert input .md file into .html output file.'''
    input_list = line_parse(input_file)
    html_lines = []
    for line in input_list:
        if line.startswith("#"):
            level = len(line.split(" ")[0])
            text = line[level:].strip()
            line_output = f"<h{level}>{text}</h{level}>"
            html_lines.append(line_output)
    return html_lines


def copy_into_html(md_file, html_file):
    '''Copy converted markdown into html file'''
    html_lines = convert_md_to_html(md_file)
    with open(html_file, "w", encoding="UTF-8") as file:
        for i, line in enumerate(html_lines):
            if i < len(html_lines) - 1:
                file.write(line + "\n")
            else:
                file.write(line)


def main():
    '''main function'''
    if len(sys.argv) != 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        sys.exit(1)

    input_md = sys.argv[1]
    output_html = sys.argv[2]

    if not os.path.isfile(input_md):
        sys.stderr.write(f"Missing {input_md}\n")
        sys.exit(1)

    copy_into_html(input_md, output_html)

    sys.exit(0)


if __name__ == '__main__':
    main()
