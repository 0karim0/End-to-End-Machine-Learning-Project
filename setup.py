import setuptools

# Read the contents of the README.md file to use it as the long description for the package
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# Define the version of the package
__version__ = "0.0.0"

# Define the repository name, author's GitHub username, source repository directory, and author's email
REPO_NAME = "End-to-end-ML-Project"
AUTHOR_USER_NAME = "Karim"
SRC_REPO = "mlProject"
AUTHOR_EMAIL = "karimhazem321@gmail.com"

# Use setuptools to define the package setup
setuptools.setup(
    # Name of the package
    name=SRC_REPO,
    # Version of the package
    version=__version__,
    # Author's name
    author=AUTHOR_USER_NAME,
    # Author's email
    author_email=AUTHOR_EMAIL,
    # Short description of the package
    description="A small python package for ml app",
    # Long description of the package (from README.md)
    long_description=long_description,
    # Format of the long description
    long_description_content="text/markdown",
    # URL of the repository
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    # Additional URLs such as bug tracker
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    # Define the root directory of the package
    package_dir={"": "src"},
    # Automatically find all packages in the 'src' directory
    packages=setuptools.find_packages(where="src")
)
