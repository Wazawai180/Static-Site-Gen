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

if __name__ == '__main__':
    unittest.main()