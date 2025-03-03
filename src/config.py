import os
import json

class Config:
    """
    Singleton class to manage configuration settings for the Noke application.
    Loads configuration from a JSON file and a default message from a text file.
    """
    # Singleton instance behavior
    _instance = None
    _config_dir = os.path.expanduser("~/.config/noke")
    _config_path = os.path.join(_config_dir, "noke_config.json")
    _default_message_path = os.path.join(_config_dir, ".default")
    
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Config, cls).__new__(cls)
        return cls._instance


    def __init__(self):
        if hasattr(self, '_initialized') and self._initialized:
            return

        self.default_file_format = ".txt"
        self.editor_command = os.getenv("EDITOR", "vim")
        self.default_message = ""
        self.notes_dir = os.path.expanduser("~/noke_notes")

        # Load or create the configuration file
        if os.path.exists(self._config_path):
            self.load_config()
        else:
            self.save_config()
            self.load_config()

        # Load or create the default message file
        if os.path.exists(self._default_message_path):
            self.load_default_message()
        else:
            self.save_default_message()

        # Create the notes directory if it doesn't exist
        os.makedirs(self.notes_dir, exist_ok=True)

        self._initialized = True

    ##################################################################
    # Methods to load and save configuration settings
    ##################################################################

    def load_config(self):
        """Load configuration settings from the JSON file."""
        with open(self._config_path, 'r') as config_file:
            config_data = json.load(config_file)
            self.default_file_format = config_data.get('default_file_format', self.default_file_format)
            self.editor_command = config_data.get('editor_command', self.editor_command)
            self.notes_dir = os.path.expanduser(config_data.get('notes_dir', self.notes_dir))

    def save_config(self):
        """Save configuration settings to the JSON file."""
        config_data = {
            'default_file_format': self.default_file_format,
            'editor_command': self.editor_command,
            'notes_dir': self.notes_dir
        }
        os.makedirs(self._config_dir, exist_ok=True)
        with open(self._config_path, 'w') as config_file:
            json.dump(config_data, config_file)

    ##################################################################
    # Methods to get configuration settings
    ##################################################################

    def load_default_message(self):
        """Load the default message from the text file."""
        with open(self._default_message_path, 'r') as default_file:
            self.default_message = default_file.read()

    def save_default_message(self):
        """Save the default message to the text file."""
        with open(self._default_message_path, 'w') as default_file:
            default_file.write(self.default_message)

    def get_default_file_format(self):
        """Return the default file format."""
        return self.default_file_format

    def get_editor_command(self):
        """Return the command to open the editor."""
        return self.editor_command

    def get_default_message(self):
        """Return the default message."""
        return self.default_message

    def get_notes_dir(self):
        """Return the notes directory path."""
        return self.notes_dir