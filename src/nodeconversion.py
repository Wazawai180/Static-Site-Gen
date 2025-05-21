from textnode import *
from htmlnode import *

def convert_text_node_to_html_node(text_node):
    if text_node.text_type == TextType.TEXT:
        return LeafNode(tag=None, value=text_node.text)
    elif text_node.text_type == TextType.BOLD:
        return LeafNode(tag="strong", value=text_node.text)
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode(tag="em", value=text_node.text)
    elif text_node.text_type == TextType.CODE:
        return LeafNode(tag="code", value=text_node.text)
    elif text_node.text_type == TextType.LINK:
        return LeafNode(tag="a", value=text_node.text, props={"href": text_node.url})
    elif text_node.text_type == TextType.IMAGE:
        return LeafNode(tag="img", value=None, props={"src": text_node.url, "alt": text_node.text})
    else:
        raise ValueError(f"Unknown TextType: {text_node.text_type}")
    
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        splits = []
        sections = node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown syntax, no closing delimiter")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                splits.append(TextNode(sections[i], TextType.TEXT))
            else:
                splits.append(TextNode(sections[i], text_type))
        new_nodes.extend(splits)
    return new_nodes

