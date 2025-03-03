import os
import json
from config import Config

class Project:
    def __init__(self, name, path):
        self.name = name
        self.path = path

    def __repr__(self):
        return f"Project(name={self.name}, path={self.path})"

class Projects:
    _instance = None
    _projects_file = os.path.expanduser("~/.config/noke/projects.json")

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Projects, cls).__new__(cls)
            cls._instance._projects = {}
            cls._instance._load_projects()
        return cls._instance

    def _load_projects(self):
        if os.path.exists(self._projects_file):
            with open(self._projects_file, 'r') as file:
                projects_data = json.load(file)
                for name, path in projects_data.items():
                    self._projects[name] = Project(name, path)

    def _save_projects(self):
        projects_data = {name: project.path for name, project in self._projects.items()}
        os.makedirs(os.path.dirname(self._projects_file), exist_ok=True)
        with open(self._projects_file, 'w') as file:
            json.dump(projects_data, file)

    def add_project(self, name, path=None):
        if name in self._projects:
            raise ValueError(f"Project with name '{name}' already exists.")
        
        config = Config()
        default_dir = config.get_notes_dir()
        project_dir = os.path.join(default_dir, name) if path is None else path

        if os.path.exists(project_dir):
            if os.listdir(project_dir):
                print(f"\033[93mWarning: Directory '{project_dir}' already exists and is not empty.\033[0m")
            else:
                print(f"\033[93mWarning: Directory '{project_dir}' already exists and is empty.\033[0m")
        else:
            os.makedirs(project_dir, exist_ok=True)

        self._projects[name] = Project(name, project_dir)
        self._save_projects()

    def remove_project(self, name):
        if name not in self._projects:
            raise ValueError(f"Project with name '{name}' does not exist.")
        del self._projects[name]
        self._save_projects()

    def get_project(self, name):
        return self._projects.get(name)

    def list_projects(self):
        return list(self._projects.values())
