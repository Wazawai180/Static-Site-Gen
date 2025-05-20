import unittest
from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("div", "Hello, World!", [], {"class": "greeting", "id": "main"})
        self.assertEqual(node.props_to_html(), ' class="greeting" id="main"')

    def test_props_to_html_empty(self):
        node = HTMLNode("div", "Hello, World!", [], {})
        self.assertEqual(node.props_to_html(), '')

    def test_props_to_html_none(self):
        node = HTMLNode("div", "Hello, World!", [], None)
        self.assertEqual(node.props_to_html(), '')

    def test_props_to_html_with_none_value(self):
        node = HTMLNode("div", "Hello, World!", [], {"class": None})
        self.assertEqual(node.props_to_html(), ' class="None"')

    def test_props_to_html_with_none_key(self):
        node = HTMLNode("div", "Hello, World!", [], {None: "value"})
        self.assertEqual(node.props_to_html(), ' None="value"')

    def test_repr(self):
        node = HTMLNode("div", "Hello, World!", [], {"class": "greeting"})
        self.assertEqual(repr(node), "HTMLNode(tag=div, value=Hello, World!, children=[], props={'class': 'greeting'})")
    
    def test_repr_with_children(self):
        child_node = HTMLNode("span", "Child", [], {"class": "child"})
        node = HTMLNode("div", "Hello, World!", [child_node], {"class": "greeting"})
        self.assertEqual(repr(node), "HTMLNode(tag=div, value=Hello, World!, children=[HTMLNode(tag=span, value=Child, children=[], props={'class': 'child'})], props={'class': 'greeting'})")
    
    def test_repr_with_empty_children(self):
        node = HTMLNode("div", "Hello, World!", [], {"class": "greeting"})
        self.assertEqual(repr(node), "HTMLNode(tag=div, value=Hello, World!, children=[], props={'class': 'greeting'})")

    def test_repr_with_empty_props(self):
        node = HTMLNode("div", "Hello, World!", [], {})
        self.assertEqual(repr(node), "HTMLNode(tag=div, value=Hello, World!, children=[], props={})")

    def test_repr_with_none_value(self):
        node = HTMLNode("div", None, [], {"class": "greeting"})
        self.assertEqual(repr(node), "HTMLNode(tag=div, value=None, children=[], props={'class': 'greeting'})")

    def test_repr_with_none_tag(self):
        node = HTMLNode(None, "Hello, World!", [], {"class": "greeting"})
        self.assertEqual(repr(node), "HTMLNode(tag=None, value=Hello, World!, children=[], props={'class': 'greeting'})")

    def test_repr_with_none_props(self):
        node = HTMLNode("div", "Hello, World!", [], None)
        self.assertEqual(repr(node), "HTMLNode(tag=div, value=Hello, World!, children=[], props={})")

    def test_repr_with_none_children(self):
        node = HTMLNode("div", "Hello, World!", None, {"class": "greeting"})
        self.assertEqual(repr(node), "HTMLNode(tag=div, value=Hello, World!, children=[], props={'class': 'greeting'})")

    def test_leaf_to_html_none(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node. to_html(), "Hello, world!")

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_b(self):
        node = LeafNode("b", "Hello, world!")
        self.assertEqual(node.to_html(), "<b>Hello, world!</b>")

    def test_leaf_to_html_i(self):
        node = LeafNode("i", "Hello, world!")
        self.assertEqual(node.to_html(), "<i>Hello, world!</i>")

if __name__ == "__main__":
    unittest.main()