from textnode import TextNode, TextType

def main():
    # Create a TextNode object
    text_node = TextNode("Hello, World!", TextType.LINK, "https://example.com")
    
    # Print the TextNode object
    print(text_node)

if __name__ == "__main__":
    main()