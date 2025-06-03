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
    
    # Tests for split_nodes_image and split_nodes_link functions
    def test_split_image(self):
        node = TextNode("This is ![image](https://i.imgur.com/zjjcJKZ.png) text", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" text", TextType.TEXT),
            ]
            , new_nodes
        )
    
    def test_split_image_no_image(self):
        node = TextNode("This is text without an image", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual([node], new_nodes)

    def test_split_image_multiple(self):
        node = TextNode(
            "This is ![image1](https://i.imgur.com/zjjcJKZ.png) and ![image2](https://i.imgur.com/zjjcJKZ.png) text",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("image1", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and ", TextType.TEXT),
                TextNode("image2", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" text", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_link(self):
        node = TextNode("This is a [link](https://example.com) text", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://example.com"),
                TextNode(" text", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_link_no_link(self):
        node = TextNode("This is text without a link", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual([node], new_nodes)

    def test_split_link_multiple(self):
        node = TextNode(
            "This is a [link1](https://example.com) and [link2](https://example.com) text",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is a ", TextType.TEXT),
                TextNode("link1", TextType.LINK, "https://example.com"),
                TextNode(" and ", TextType.TEXT),
                TextNode("link2", TextType.LINK, "https://example.com"),
                TextNode(" text", TextType.TEXT),
            ],
            new_nodes,
        )

    # Tests for the extract_markdown_images function
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_images_no_image(self):
        matches = extract_markdown_images("This is text without an image")
        self.assertListEqual([], matches)

    def test_extract_markdown_images_multiple(self):
        matches = extract_markdown_images(
            "This is text with an ![image1](https://i.imgur.com/zjjcJKZ.png) and ![image2](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual(
            [
                ("image1", "https://i.imgur.com/zjjcJKZ.png"),
                ("image2", "https://i.imgur.com/zjjcJKZ.png"),
            ],
            matches,
        )

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://example.com)"
        )
        self.assertListEqual([("link", "https://example.com")], matches)

    def test_extract_markdown_links_no_link(self):
        matches = extract_markdown_links("This is text without a link")
        self.assertListEqual([], matches)

    def test_extract_markdown_links_multiple(self):
        matches = extract_markdown_links(
            "This is text with a [link1](https://example.com) and [link2](https://example.com)"
        )
        self.assertListEqual(
            [
                ("link1", "https://example.com"),
                ("link2", "https://example.com"),
            ],
            matches,
        )

    # Test cases for text to text node conversion functions
    def test_text_to_text_node_conversion(self):
        nodes = text_to_textnodes(
            "This is **text** with an _italic_ word and a `code block` and an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://boot.dev)"
        )
        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
            nodes,
        )
    

if __name__ == "__main__":
    unittest.main()



