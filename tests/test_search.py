import unittest
from src.search import extract_keywords, search_notes

class TestSearchFunctionality(unittest.TestCase):

    def test_extract_keywords(self):
        note = "This is a sample note for testing keyword extraction."
        expected_keywords = {"sample", "note", "testing", "keyword", "extraction"}
        self.assertEqual(extract_keywords(note), expected_keywords)

    def test_search_notes_found(self):
        notes = [
            "This is a sample note.",
            "Another note for testing.",
            "Testing keyword search functionality."
        ]
        keyword = "testing"
        expected_results = [
            "Another note for testing.",
            "Testing keyword search functionality."
        ]
        self.assertEqual(search_notes(notes, keyword), expected_results)

    def test_search_notes_not_found(self):
        notes = [
            "This is a sample note.",
            "Another note for testing.",
            "Testing keyword search functionality."
        ]
        keyword = "nonexistent"
        expected_results = []
        self.assertEqual(search_notes(notes, keyword), expected_results)

if __name__ == '__main__':
    unittest.main()