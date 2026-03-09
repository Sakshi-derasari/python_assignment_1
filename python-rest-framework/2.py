# 2. Write a Python script to set up a Django project and install packages like django, djangorestframework, requests, etc.

import os
import subprocess
import sys

def run_command(command):
    print(f"\n Running: {command}\n")
    process = subprocess.Popen(command, shell=True)
    process.communicate()

def main():
    project_name = "myproject"

    # 1. Create virtual environment
    print("Creating virtual environment...")
    run_command(f"{sys.executable} -m venv venv")

    # 2. Activate virtual environment
    print("Activating virtual environment...")
    if os.name == "nt":  # Windows
        activate_cmd = r".\venv\Scripts\activate"
    else:  # macOS/Linux
        activate_cmd = "source venv/bin/activate"

    # 3. Install required packages
    print("Installing packages: django, djangorestframework, requests")
    run_command(f"{activate_cmd} && pip install django djangorestframework requests")

    # 4. Create Django project
    print(f"Creating Django project: {project_name}")
    run_command(f"{activate_cmd} && django-admin startproject {project_name}")

    print("\n project is ready.")
    print(f"start working:\n   {activate_cmd}\n   cd {project_name}\n   python manage.py runserver")

if __name__ == "__main__":
    main()