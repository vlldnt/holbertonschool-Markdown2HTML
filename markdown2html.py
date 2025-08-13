#!/usr/bin/python3
'''Markdown to HTML converter script'''

import sys
import os
import hashlib
import re

def line_parse(input_file):
    '''Parse lines inside the README.md (input_file)'''
    with open(input_file, "r", encoding='utf-8') as file:
        return [line.rstrip("\n") for line in file]


def paragraph_change(text):
    """Convert markdown bold/italic """
    
    # Handling the remove of the letter c and C  : ((<STRING>)) 
    pattern_parentheses = r'\(\((.*?)\)\)'
    while True:
        match = re.search(pattern_parentheses, text)
        if not match:
            break
        content = match.group(1)
        processed_content = re.sub(r'(\*\*c\*\*|\*\*C\*\*|\_\_c\_\_|\_\_C\_\_|c|C)', '', content)
        text = text.replace(match.group(0), processed_content, 1)
    
    # Handling the MD5 conversion : [[<STRING>]]
    pattern = r'\[\[(.*?)\]\]'
    while True:
        match_pattern = re.search(pattern, text)
        if not match_pattern:
            break
        full_match = match_pattern.group(0)
        content = match_pattern.group(1)
        md5 = hashlib.md5(content.encode()).hexdigest()
        text = text.replace(full_match, md5, 1)    
    
    # Bold handling (**<STRING>**)
    while "**" in text:
        text = text.replace("**", "<b>", 1)
        if "**" in text:
            text = text.replace("**", "</b>", 1)

    # Emphasized handling (__<STRING>__)
    while "__" in text:
        text = text.replace("__", "<em>", 1)
        if "__" in text:
            text = text.replace("__", "</em>", 1)

    return text


def convert_md_to_html(input_file):
    """Convert input md syntac into html syntax"""
    input_list = line_parse(input_file)
    html_lines = []
    in_list = False
    list_tag = None
    in_paragraph = False

    for line in input_list:
        stripped = line.strip()

        # Title handling (#, ##, ###, ####, #####, ######)
        if stripped.startswith("#"):
            if in_list:
                html_lines.append(f"</{list_tag}>")
                in_list = False
            if in_paragraph:
                html_lines.append("</p>")
                in_paragraph = False

            level = len(stripped.split(" ")[0])
            text = stripped[level:].strip()
            html_lines.append(f"<h{level}>{paragraph_change(text)}</h{level}>")

        # Unordered list (- )
        elif stripped.startswith('- '):
            text = paragraph_change(stripped[2:])
            if not in_list or list_tag != "ul":
                if in_list:
                    html_lines.append(f"</{list_tag}>")
                html_lines.append("<ul>")
                in_list = True
                list_tag = "ul"
            html_lines.append(f"\t<li>{text}</li>")

        # Ordered list (* )
        elif stripped.startswith('* '):
            text = paragraph_change(stripped[2:])
            if not in_list or list_tag != "ol":
                if in_list:
                    html_lines.append(f"</{list_tag}>")
                html_lines.append("<ol>")
                in_list = True
                list_tag = "ol"
            html_lines.append(f"\t<li>{text}</li>")

        # Paragraph text (p / br)
        else:
            if in_list:
                html_lines.append(f"</{list_tag}>")
                in_list = False
            if stripped:
                if not in_paragraph:
                    html_lines.append("<p>")
                    in_paragraph = True
                else:
                    html_lines.append(f"\t<br />")
                html_lines.append(f"\t{paragraph_change(stripped)}")
            else:
                if in_paragraph:
                    html_lines.append("</p>")
                    in_paragraph = False

    # Closing opened tag
    if in_list:
        html_lines.append(f"</{list_tag}>")
    if in_paragraph:
        html_lines.append("</p>")

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
    '''Main function'''
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
