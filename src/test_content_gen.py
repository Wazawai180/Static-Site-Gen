import unittest
from content_gen import extract_title

class TestContentGen(unittest.TestCase):
    # Test cases for extract title
    def test_eq(self):
        actual = extract_title("# This is a title")
        self.assertEqual(actual, "This is a title")

    def test_extract_title(self):
        title = extract_title(
            "# This is a title\n\nThis is the content of the document."
        )
        self.assertEqual(title, "This is a title")

    def test_extract_title_no_title(self):
        with self.assertRaises(Exception) as context: 
            extract_title("This is the content of the document without a title.")
        self.assertIn("No title found in the text. Make sure the title is the first line and starts with '# '.", str(context.exception))

    def test_extract_title_empty_text(self):
        with self.assertRaises(Exception) as context:
            extract_title("")
        self.assertIn("No lines found in the text.", str(context.exception))

if  __name__ == "__main__":
    unittest.main()