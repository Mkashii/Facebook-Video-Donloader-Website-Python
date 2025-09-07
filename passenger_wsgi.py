import sys
import os

# Set the path to the virtual environment
virtualenv_path = '/home/fdownload/myenv'  # Path to your new virtual environment

# Ensure the correct Python version is being used
sys.executable = os.path.join(virtualenv_path, 'bin', 'python3.11')

# Add the virtual environment's site-packages to the system path (use Python 3.11 version here)
sys.path.insert(0, os.path.join(virtualenv_path, 'lib', 'python3.11', 'site-packages'))

# Add the application directory to the system path
sys.path.insert(0, '/home/fdownload/fbdownload')  # Path to your app directory

# Add the virtual environment's bin directory to the system path (for executables)
sys.path.insert(0, os.path.join(virtualenv_path, 'bin'))

# Import the Flask application (make sure to replace 'app' with the correct entry point if needed)
from app import app as application  # Assuming the app is in 'app.py' and the app object is named 'app'
