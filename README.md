# cookiecutter-fastapi

<div align="center">
    <img src="readme_resources/README.png" alt="AWS Utils" width="200"/>
</div>

## Overview:
Cookiecutter module with Fast API starter kit
    - url: https://cookiecutter.readthedocs.io/en/stable/


## Project Structure:
```
cookiecutter-fastapi/
      │
      ├── hooks/
      │     ├── post_gen_project.py  # Post-generation hook script for project setup
      │     ├── pre_gen_project.py  # Pre-generation hook script for project setup
      │     └── pre_prompt.py  # Pre-prompt hook script for project setup 
      │
      ├── readme_resources/
      │     └── README.png    # Picture for the Read me file
      │
      ├── {{cookiecutter.project_slug}}/
      │           └── README.png
      │                 │
      │                 ├── fastapi/
      │                 │        └── app.py  # Main application file for Fast API
      │                 │
      │                 │
      │                 ├── readme_resources/
      │                 │        └── README.png    # Picture for the Read me file
      │                 │
      │                 ├── .gitignore  # Git ignore file to exclude unnecessary files from version control
      │                 ├── AUTHORS   # File listing project contributors
      │                 ├── MANIFEST.in  # File specifying additional files to include in the distribution
      │                 ├── README.md   # README file for project documentation
      │                 └── requirements.txt  # Python dependencies for the project
      │
      │
      ├── .gitignore  # Git ignore file to exclude unnecessary files from version control
      ├── cookiecutter.json  # Cookiecutter configuration file defining project variables and structure
      ├── README.md   # README file for project documentation
      └── requirements.txt  # Python dependencies for the project
```