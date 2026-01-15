from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import os

# Get absolute paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FRONTEND_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "frontend"))

app = Flask(
    __name__,
    static_folder=FRONTEND_DIR,
    template_folder=FRONTEND_DIR
)

CORS(app)

menu = [
    {"id": 1, "name": "Pizza", "price": 299, "image": "images/pizza.jpg"},
    {"id": 2, "name": "Burger", "price": 149, "image": "images/Burger.jpg"},
    {"id": 3, "name": "Biryani", "price": 249, "image": "images/Biryani.jpg"}
]

@app.route("/menu")
def get_menu():
    return jsonify(menu)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
