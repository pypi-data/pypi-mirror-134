import os
import pathlib
from dotenv import load_dotenv

path = pathlib.Path(os.path.realpath(__file__))
path = str(path.parent) + "/app.py"

os.environ['FLASK_APP'] = path  # Set environment variable

dotenv_path = join(dirname(__file__), '.env')  # Path to .env file
load_dotenv(dotenv_path)
