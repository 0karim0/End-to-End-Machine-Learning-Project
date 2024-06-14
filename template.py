import os
from pathlib import Path
import logging

# Configure logging to display the timestamp and message for each log entry
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# Define the project name
project_name = "mlProject"

# List of files and their paths that need to be created for the project
list_of_files = [
    ".github/workflows/.gitkeep",                 # Placeholder for GitHub Actions workflows
    f"src/{project_name}/__init__.py",            # Init file for the main project module
    f"src/{project_name}/components/__init__.py", # Init file for components submodule
    f"src/{project_name}/utils/__init__.py",      # Init file for utils submodule
    f"src/{project_name}/utils/common.py",        # Common utility functions
    f"src/{project_name}/config/__init__.py",     # Init file for config submodule
    f"src/{project_name}/config/configuration.py",# Configuration related code
    f"src/{project_name}/pipeline/__init__.py",   # Init file for pipeline submodule
    f"src/{project_name}/entity/__init__.py",     # Init file for entity submodule
    f"src/{project_name}/entity/config_entity.py",# Configuration entity definitions
    f"src/{project_name}/constants/__init__.py",  # Init file for constants submodule
    "config/config.yaml",                         # YAML configuration file
    "params.yaml",                                # Parameters file
    "schema.yaml",                                # Schema definition file
    "main.py",                                    # Main entry point for the application
    "app.py",                                     # Application entry point (e.g., for a web server)
    "Dockerfile",                                 # Docker configuration file
    "requirements.txt",                           # Python dependencies
    "setup.py",                                   # Setup script for the project
    "research/trials.ipynb",                      # Jupyter notebook for experiments and trials
    "templates/index.html",                       # HTML template file
    "test.py"                                     # Testing script
]

# Loop through the list of files to create directories and files as needed
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)  # Split the file path into directory and file name

    # Create the directory if it doesn't exist
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    # Create the file if it doesn't exist or is empty
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass  # Create an empty file
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")
