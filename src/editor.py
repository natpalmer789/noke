# filepath: /file-editor-cli/file-editor-cli/src/editor.py

import os
import subprocess

def open_file_in_editor(file_path):
    """Open a file in the terminal's default editor."""
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    try:
        subprocess.run([os.environ.get('EDITOR', 'nano'), file_path], check=True)
    except Exception as e:
        raise RuntimeError(f"Failed to open the editor: {e}")

def save_file(file_path, content):
    """Save content to a file."""
    with open(file_path, 'w') as file:
        file.write(content)