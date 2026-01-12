from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import os

# Absolute path to project root
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Frontend folder path
FRONTEND_DIR = os.path.join(PROJECT_ROOT, "frontend")

print("PROJECT_ROOT:", PROJECT_ROOT)
print("FRONTEND_DIR:", FRONTEND_DIR)
print("INDEX EXISTS:", os.path.exists(os.path.join(FRONTEND_DIR, "index.html")))

app = Flask(__name__, static_folder=FRONTEND_DIR, static_url_path="")
CORS(app)

menu = [
    {"id": 1, "name": "Pizza", "price": 299, "image": "/images/pizza.jpg"},
    {"id": 2, "name": "Burger", "price": 149, "image": "/images/Burger.jpg"},
    {"id": 3, "name": "Biryani", "price": 249, "image": "/images/Biryani.jpg"}
]

@app.route("/menu")
def get_menu():
    return jsonify(menu)

@app.route("/order/<item>", methods=["POST"])
def order(item):
    return jsonify({"message": f"Order placed successfully for {item}"})

# Serve index.html at root
@app.route("/")
def home():
    return send_from_directory(FRONTEND_DIR, "index.html")

# Serve JS, CSS, images
@app.route("/<path:path>")
def static_files(path):
    return send_from_directory(FRONTEND_DIR, path)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
