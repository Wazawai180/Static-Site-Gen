import unittest
from textnode import *
from htmlnode import *
from nodeconversion import *

class TestNodeConversion(unittest.TestCase):
    
    # Tests for the convert_text_node_to_html_node function
    def test_convert_text_node_to_html_node_normal(self):
        text_node = TextNode("Hello, World!", TextType.TEXT)
        html_node = convert_text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "Hello, World!")
        self.assertEqual(html_node.props, {})

    def test_convert_text_node_to_html_node_bold(self):
        text_node = TextNode("Hello, World!", TextType.BOLD)
        html_node = convert_text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "strong")
        self.assertEqual(html_node.value, "Hello, World!")
        self.assertEqual(html_node.props, {})

    def test_convert_text_node_to_html_node_italic(self):
        text_node = TextNode("Hello, World!", TextType.ITALIC)
        html_node = convert_text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "em")
        self.assertEqual(html_node.value, "Hello, World!")
        self.assertEqual(html_node.props, {})

    def test_convert_text_node_to_html_node_code(self):
        text_node = TextNode("Hello, World!", TextType.CODE)
        html_node = convert_text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "Hello, World!")
        self.assertEqual(html_node.props, {})

    def test_convert_text_node_to_html_node_link(self):
        text_node = TextNode("Hello, World!", TextType.LINK, "http://example.com")
        html_node = convert_text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Hello, World!")
        self.assertEqual(html_node.props, {"href": "http://example.com"})

    def test_convert_text_node_to_html_node_image(self):
        text_node = TextNode("Hello, World!", TextType.IMAGE, "http://example.com/image.png")
        html_node = convert_text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, None)
        self.assertEqual(html_node.props, {"src": "http://example.com/image.png", "alt": "Hello, World!"})

    # Tests for the split_nodes_delimiter function
    def test_split_nodes_delim_normal(self):
        text_node = TextNode("This is normal text", TextType.TEXT)
        result = split_nodes_delimiter([text_node], "*", TextType.ITALIC)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].text, "This is normal text")
        self.assertEqual(result[0].text_type, TextType.TEXT)

    def test_split_nodes_delim_bold(self):
        text_node = TextNode("This is **bold** text", TextType.TEXT)
        result = split_nodes_delimiter([text_node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" text", TextType.TEXT),
            ],
            result,
        )

    def test_split_nodes_delim_double_bold(self):
        text_node = TextNode("This is **bold** text and more **bold** text", TextType.TEXT)
        result = split_nodes_delimiter([text_node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" text and more ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" text", TextType.TEXT),
            ],
            result,
        )

    def test_split_nodes_delim_multiword_bold(self):
        text_node = TextNode("This is **bold** text and **more bold text**", TextType.TEXT)
        result = split_nodes_delimiter([text_node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" text and ", TextType.TEXT),
                TextNode("more bold text", TextType.BOLD),
            ],
            result,
        )

    def test_split_nodes_delim_italic(self):
        text_node = TextNode("This is _italic_ text", TextType.TEXT)
        result = split_nodes_delimiter([text_node], "_", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" text", TextType.TEXT),
            ],
            result,
        )

    def test_split_nodes_delim_bold_and_italic(self):
        text_node = TextNode("**bold** and _italic_", TextType.TEXT)
        result = split_nodes_delimiter([text_node], "**", TextType.BOLD)
        result = split_nodes_delimiter(result, "_", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
            ],
            result,
        )

    def test_split_nodes_delim_code(self):
        text_node = TextNode("This is `code` text", TextType.TEXT)
        result = split_nodes_delimiter([text_node], "`", TextType.CODE)
        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("code", TextType.CODE),
                TextNode(" text", TextType.TEXT),
            ],
            result,
        )

if __name__ == "__main__":
    unittest.main()



