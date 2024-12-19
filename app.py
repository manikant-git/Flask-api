from flask import Flask
from views import *

app = Flask(__name__)

# Root route to prevent 404 for / requests
@app.route('/')
def home():
    return "Library Management System API is running!"

# Include other routes from the views.py (CRUD operations, etc.)
if __name__ == '__main__':
    app.run(debug=True)

