
# <img src="https://cdn.prod.website-files.com/6105315644a26f77912a1ada/63eea844ae4e3022154e2878_Holberton-p-500.png" width="140px" alt="Holberton School"> - Markdown to HTML

Markdown (.md) to HTML converter, created as part of the Holberton School curriculum.

## Description

This project provides a Python script to transform a Markdown file into an HTML file, supporting the main Markdown syntaxes:

- Headings (`#`, `##`, ..., `######`)
- Unordered lists (`-`)
- Ordered lists (`*`)
- Paragraphs and line breaks
- Bold text (`**text**`)
- Emphasis text (`__text__`)
- Advanced features:
	- `[[text]]`: converts the text to MD5
	- `((text))`: removes all "c" or "C" letters from the text

## Usage

```bash
./markdown2html.py input_markdown.md output_html.html
```

- If the number of arguments is incorrect:  
	Prints `Usage: ./markdown2html.py README.md README.html` to STDERR and exits with code 1.
- If the Markdown file does not exist:  
	Prints `Missing <filename>` to STDERR and exits with code 1.
- Otherwise, the script converts the Markdown file to HTML and exits with code 0.

## Examples

### Headings

Markdown:
```
# Title 1
## Title 2
```
HTML:
```html
<h1>Title 1</h1>
<h2>Title 2</h2>
```

### Lists

Markdown:
```
- Item 1
- Item 2
* Item 3
* Item 4
```
HTML:
```html
<ul>
<li>Item 1</li>
<li>Item 2</li>
</ul>
<ol>
<li>Item 3</li>
<li>Item 4</li>
</ol>
```

### Paragraphs and text

Markdown:
```
Simple text

Text on
multiple lines
```
HTML:
```html
<p>
Simple text
</p>
<p>
Text on
<br/>
multiple lines
</p>
```

### Bold and emphasis

Markdown:
```
**Bold**
__Emphasis__
```
HTML:
```html
<b>Bold</b>
<em>Emphasis</em>
```

### Advanced features

Markdown:
```
[[secret]]
((Caracas))
```
HTML:
```html
<p>
8b1a9953c4611296a827abf8c47804d7
</p>
<p>
araas
</p>
```

## Constraints

- Compatible with Ubuntu 18.04 LTS, Python 3.7+
- Follows PEP8
- All files are executable and documented
- No code is executed when the module is imported

---

<img src="https://cdn.prod.website-files.com/64107f65f30b69371e3d6bfa/65c6179aa44b63fa4f31e7ad_Holberton-Logo-Cherry.svg" width="200px" alt="Holberton Logo Cherry">
