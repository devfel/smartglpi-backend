import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
GLPI_API_URL = os.getenv("GLPI_API_URL")
GLPI_API_APP_TOKEN = os.getenv("GLPI_API_APP_TOKEN")
GLPI_API_USER_TOKEN = os.getenv("GLPI_API_USER_TOKEN")
