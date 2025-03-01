def save_note_to_file(note, filename):
    with open(filename, 'a') as file:
        file.write(note + '\n')

def load_notes_from_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        return []

def clear_notes_file(filename):
    open(filename, 'w').close()