import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

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

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span><b>grandchild</b></span></div>")

    def test_to_html_with_none_grandchildren(self):
        child_node = ParentNode("span", None)
        parent_node = ParentNode("div", [child_node])
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_to_html_with_grandchildren_none_tag(self):
        grandchild_node = LeafNode(None, "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>grandchild</span></div>")

    def test_to_html_with_grandchildren_none_value(self):
        grandchild_node = LeafNode("b", None)
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_to_html_with_grandchildren_none_props(self):
        grandchild_node = LeafNode("b", "grandchild", None)
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span><b>grandchild</b></span></div>")

    def test_to_html_with_grandchildren_empty_props(self):
        grandchild_node = LeafNode("b", "grandchild", {})
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span><b>grandchild</b></span></div>")

    def test_to_html_with_props(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node], {"class": "parent"})
        self.assertEqual(parent_node.to_html(), '<div class="parent"><span>child</span></div>')
    
    def test_to_html_with_none_tag(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode(None, [child_node])
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_to_html_with_none_children(self):
        parent_node = ParentNode("div", None)
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_to_html_with_none_value(self):
        parent_node = ParentNode("div", [])
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_to_html_with_empty_children(self):
        parent_node = ParentNode("div", [])
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_to_html_with_empty_props(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node], {})
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")
    
    def test_to_html_with_none_props(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node], None)
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

if __name__ == "__main__":
    unittest.main()