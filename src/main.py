import argparse
import os
from config import Config

def parse_arguments():
    parser = argparse.ArgumentParser(description='Command line utility for editing notes.')
    parser.add_argument('new', type=str, help='Name of the new file to create')
    parser.add_argument('-v', '--verbosity', action='store_true', help='Enable verbose output')
    return parser.parse_args()

def main():
    # Initialize the Config singleton
    config = Config()
    
    # Parse command line arguments
    args = parse_arguments()
    
    # Check if verbosity mode is enabled
    if args.verbosity:
        print("Verbose mode enabled")
    
    # Get the default file format and message from the config
    file_format = config.get_default_file_format()
    default_message = config.get_default_message()
    notes_dir = config.get_notes_dir()
    
    # Append the file format to the new file name if not already present
    if not args.new.endswith(file_format):
        args.new += file_format

    # Get the notes_dir path
    new_file_path = os.path.join(notes_dir, args.new)

    # Expand the user path
    new_file_path = os.path.expanduser(new_file_path)
    
    print(new_file_path)

    # Check if the file already exists
    if os.path.isfile(new_file_path):
        print("File already exists. Opening the file with the editor.")
        os.system(f"{config.get_editor_command()} {new_file_path}")
        return

    # Write the default message to the new file
    with open(new_file_path, 'x') as new_file:
        new_file.write(default_message)
        new_file.close()

    print("New File created at {}".format(new_file_path))
    
    # Open the file with the editor
    os.system(f"{config.get_editor_command()} {new_file_path}")

if __name__ == '__main__':
    main()