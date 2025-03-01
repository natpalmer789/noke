# filepath: /home/palmer/file-editor-cli/file-editor-cli/src/search.py

import re
from collections import Counter

def extract_keywords(text):
    """Extract keywords from the given text."""
    # Normalize the text to lowercase and remove punctuation
    text = re.sub(r'[^\w\s]', '', text.lower())
    words = text.split()
    
    # Count the frequency of each word
    word_counts = Counter(words)
    
    # Return the most common words as keywords
    return word_counts.most_common()

def search_notes(notes, keyword):
    """Search for notes containing the given keyword."""
    results = []
    for note in notes:
        if keyword.lower() in note.lower():
            results.append(note)
    return results