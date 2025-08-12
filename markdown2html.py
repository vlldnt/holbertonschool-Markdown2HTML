#!/usr/bin/python3
'''Markdown to HTML converter script'''


import sys
import os


def main():
    if len(sys.argv) < 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        sys.exit(1)

    input_md = sys.argv[1]
    output_html = sys.argv[2]

    if not os.path.isfile(input_md):
        sys.stderr.write(f"Missing {input_md}\n")
        sys.exit(1)

    sys.exit(0)


if __name__ == '__main__':
    main()
