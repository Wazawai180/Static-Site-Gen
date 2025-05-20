import unittest
from textnode import *
from htmlnode import *
from nodeconversion import *

class TestNodeConversion(unittest.TestCase):
    def test_convert_text_node_to_html_node_normal(self):
        text_node = TextNode("Hello, World!", TextType.NORMAL)
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
        