import os
from blocks import markdown_to_html_node
from pathlib import Path

def generate_page(src_path, template_path, dst_path, basepath):
    """
    Generates a page by reading the source markdown file, converting it to HTML,
    and writing it to the destination path using the specified template.

    :param src_path: Path to the source markdown file
    :param template_path: Path to the HTML template file
    :param dst_path: Path to the destination HTML file
    """
    print(f"Generating page from {src_path} to {dst_path} using {template_path}")

    with open(src_path, 'r', encoding='utf-8') as src_file:
        markdown_content = src_file.read()

    node = markdown_to_html_node(markdown_content)
    html = node.to_html()

    with open(template_path, 'r', encoding='utf-8') as template_file:
        template_content = template_file.read()

    title = extract_title(markdown_content)
    template_content = template_content.replace("{{ Title }}", title)
    template_content = template_content.replace("{{ Content }}", html)
    template_content = template_content.replace('href="/', 'href="' + basepath)
    template_content = template_content.replace('src="/', 'src="' + basepath)

    if dst_path != "":
        os.makedirs(os.path.dirname(dst_path), exist_ok=True)
    with open(dst_path, 'w', encoding='utf-8') as dst_file:
        dst_file.write(template_content)

def generate_pages_recursively(src_dir, template_path, dst_dir, basepath):
    """
    Recursively generates pages from markdown files in the source directory,
    using the specified template, and writes them to the destination directory.

    :param src_dir: Path to the source directory containing markdown files
    :param template_path: Path to the HTML template file
    :param dst_dir: Path to the destination directory for generated HTML files
    """
    for filename in os.listdir(src_dir):
        src_file_path = os.path.join(src_dir, filename)
        if os.path.isdir(src_file_path):
            # Recursively process subdirectories
            sub_dst_dir = os.path.join(dst_dir, filename)
            generate_pages_recursively(src_file_path, template_path, sub_dst_dir, basepath)
        elif filename.endswith('.md'):
            # Process markdown files
            dst_file_path = os.path.join(dst_dir, filename.replace('.md', '.html'))
            generate_page(src_file_path, template_path, dst_file_path, basepath)
        else:
            print(f"Skipping non-markdown file: {src_file_path}")

def extract_title(text):
    """
    Extracts the title from the text.
    The title is the first line of the text, which is expected to be a markdown header.
    """
    lines = text.splitlines()
    if not lines:
        raise Exception("No lines found in the text.")
    for line in lines:
        line = line.strip()
        if line.startswith("# "):
            return line[2:].strip()
    raise Exception("No title found in the text. Make sure the title is the first line and starts with '# '.")