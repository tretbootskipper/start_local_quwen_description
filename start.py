import subprocess
import os
import sys

# Path to your venv and script
project_dir = os.path.dirname(os.path.abspath(__file__))
venv_python = os.path.join(project_dir, "venv", "Scripts", "python.exe")
app_script = os.path.join(project_dir, "app_gui.py")

# Run the app with the venv's Python
subprocess.run([venv_python, app_script])

# Optional: Keep window open (only useful if double-clicked from Explorer)
if sys.stdin.isatty():
    input("\nPress Enter to exit...")


# this might be needed? pip install pillow (global installation, not local!)
