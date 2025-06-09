import unittest
from blocks import *

class TestMarkdownBlocks(unittest.TestCase):

    # Test cases for the blocks module
    def test_markdown_to_blocks(self):
        md = """
This is a **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- With items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is a **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- With items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is a **bolded** paragraph



This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- With items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is a **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- With items",
            ],
        )

    # Test cases for block_to_block_type function
    def test_block_to_block_types(self):
        block = "# Heading 1"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
        block = "## Heading 2"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
        block = "### Heading 3"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
        block = "#### Heading 4"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
        block = "##### Heading 5"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
        block = "###### Heading 6"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
        block = "```python\nprint('Hello, World!')\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)
        block = "> This is a quote\n> This is more quote"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
        block = "- This is a list item\n- This is another list item"
        self.assertEqual(block_to_block_type(block), BlockType.ULIST)
        block = "1. This is an ordered list item\n2. This is another ordered list item"
        self.assertEqual(block_to_block_type(block), BlockType.OLIST)
        block = "This is a paragraph with no special formatting."
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    # Test cases for markdown to html node functions
    def test_paragraph(self):
        block = """
This is a paragraph with **bold**
text and should have a p
tag here.

"""
        node = markdown_to_html_node(block)
        html = node.to_html()
        self.assertEqual(
            html,
            '<div><p>This is a paragraph with <strong>bold</strong> text and should have a p tag here.</p></div>'
        )

    def test_paragraphs(self):
        block = """
This is a paragraph with **bold**
text and should have a p
tag here.

This is another paragraph with _italic_ text and `code` here.

"""
        node = markdown_to_html_node(block)
        html = node.to_html()
        self.assertEqual(
            html,
            '<div><p>This is a paragraph with <strong>bold</strong> text and should have a p tag here.</p>'
            '<p>This is another paragraph with <em>italic</em> text and <code>code</code> here.</p></div>'
        )

    def test_heading(self):
        block = """
#This is a heading h1

this is paragraph text.

######This is a heading h6

"""
        node = markdown_to_html_node(block)
        html = node.to_html()
        self.assertEqual(
            html, '<div><h1>This is a heading h1</h1><p>this is paragraph text.</p><h6>This is a heading h6</h6></div>'
        )

    def test_lists(self):
        block = """
- This is a list item
- This is another list item
- One more ulist item

1. This is an ordered list item
2. This is another ordered list item
"""
        node = markdown_to_html_node(block)
        html = node.to_html()
        self.assertEqual(
            html,
            '<div><ul><li>This is a list item</li><li>This is another list item</li><li>One more ulist item</li></ul>'
            '<ol><li>This is an ordered list item</li><li>This is another ordered list item</li></ol></div>'
        )

    def test_quote(self):
        block = """
> This is a quote
> a blockquote with multiple lines

this is paragraph text.
"""
        node = markdown_to_html_node(block)
        html = node.to_html()
        self.assertEqual(
            html,
            '<div><blockquote>This is a quote a blockquote with multiple lines</blockquote><p>this is paragraph text.</p></div>'
        )

if __name__ == '__main__':
    unittest.main()