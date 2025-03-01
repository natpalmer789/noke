import os
import sys

# Add the path to the src directory to the system path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from main import main as main_script

def main():
    main_script()

if __name__ == "__main__":
    main()
