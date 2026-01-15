from flask import Flask, jsonify, render_template
from flask_cors import CORS
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FRONTEND_DIR = os.path.join(BASE_DIR, "..", "frontend")
STATIC_DIR = FRONTEND_DIR   # frontend itself contains static files

app = Flask(
    __name__,
    static_folder=STATIC_DIR,
    static_url_path="/static",
    template_folder=FRONTEND_DIR
)

CORS(app)

menu = [
    {"id": 1, "name": "Pizza", "price": 299, "image": "images/pizza.jpg"},
    {"id": 2, "name": "Burger", "price": 149, "image": "images/Burger.jpg"},
    {"id": 3, "name": "Biryani", "price": 249, "image": "images/Biryani.jpg"}
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/menu")
def get_menu():
    return jsonify(menu)

@app.route("/order/<item>", methods=["POST"])
def order_food(item):
    return jsonify({"message": f"{item} ordered successfully!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
