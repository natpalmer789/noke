import unittest
from src.editor import open_file, save_file

class TestEditor(unittest.TestCase):

    def test_open_file(self):
        # Test opening a file in the default editor
        result = open_file('test_note.txt')
        self.assertTrue(result)

    def test_save_file(self):
        # Test saving content to a file
        content = "This is a test note."
        result = save_file('test_note.txt', content)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()