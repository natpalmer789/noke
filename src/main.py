import argparse
import os
from config import Config
from projects import Projects

def parse_arguments():
    parser = argparse.ArgumentParser(description='Command line utility for editing notes.')
    parser.add_argument('new', nargs='?', type=str, help='Name of the new file to create')
    parser.add_argument('-v', '--verbosity', action='store_true', help='Enable verbose output')
    parser.add_argument('--add-project', type=str, help='Add a new project directory')
    parser.add_argument('--remove-project', type=str, help='Remove an existing project directory')
    return parser.parse_args()

def main():
    # Initialize the Config singleton
    config = Config()
    projects = Projects()
    
    # Parse command line arguments
    args = parse_arguments()
    
    # Check if verbosity mode is enabled
    if args.verbosity:
        print("Verbose mode enabled")
    
    # Handle project management commands
    if args.add_project:
        try:
            projects.add_project(args.add_project)
            print(f"Added project: {args.add_project}")
        except ValueError as e:
            print(e)
        return

    if args.remove_project:
        try:
            projects.remove_project(args.remove_project)
            print(f"Removed project: {args.remove_project}")
        except ValueError as e:
            print(e)
        return
    
    # If no new file is specified, list projects and exit
    if not args.new:
        print("No new file specified. Listing projects:")
        for project in projects.list_projects():
            print(project)
        return
    
    # Get the default file format and message from the config
    file_format = config.get_default_file_format()
    default_message = config.get_default_message()
    notes_dir = config.get_notes_dir()
    
    # Determine if a project directory is specified
    if '/' in args.new:
        project_name, new_file_name = args.new.split('/', 1)
        project = projects.get_project(project_name)
        if not project:
            print(f"Project '{project_name}' does not exist.")
            return
        notes_dir = project.path
    else:
        new_file_name = args.new
    
    # Append the file format to the new file name if not already present
    if not new_file_name.endswith(file_format):
        new_file_name += file_format

    # Get the notes_dir path
    new_file_path = os.path.join(notes_dir, new_file_name)

    # Expand the user path
    new_file_path = os.path.expanduser(new_file_path)
    
    print(new_file_path)

    # Ensure the project directory exists
    os.makedirs(os.path.dirname(new_file_path), exist_ok=True)

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