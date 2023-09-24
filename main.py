from flask import Flask
from flask_cors import CORS
from src import routes

app = Flask(__name__)
CORS(app)  # Enable CORS for the entire app

# Initialize the routes
routes.init_app(app)

if __name__ == "__main__":
    app.run(debug=True)
