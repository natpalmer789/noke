def validate_input(user_input):
    # Function to validate user input
    if not user_input:
        raise ValueError("Input cannot be empty.")
    return user_input.strip()

def format_note_content(note_content):
    # Function to format note content for display
    return note_content.replace('\n', ' ').strip()

def extract_keywords(note_content):
    # Function to extract keywords from note content
    words = note_content.split()
    keywords = set(word.lower() for word in words if len(word) > 3)  # Example: keywords longer than 3 characters
    return keywords