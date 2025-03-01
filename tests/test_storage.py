import unittest
from src.storage import Storage

class TestStorage(unittest.TestCase):

    def setUp(self):
        self.storage = Storage('test_notes.txt')

    def test_save_note(self):
        note = "This is a test note."
        self.storage.save(note)
        with open('test_notes.txt', 'r') as f:
            content = f.read()
        self.assertIn(note, content)

    def test_retrieve_notes(self):
        note1 = "First note."
        note2 = "Second note."
        self.storage.save(note1)
        self.storage.save(note2)
        notes = self.storage.retrieve()
        self.assertIn(note1, notes)
        self.assertIn(note2, notes)

    def tearDown(self):
        import os
        try:
            os.remove('test_notes.txt')
        except FileNotFoundError:
            pass

if __name__ == '__main__':
    unittest.main()