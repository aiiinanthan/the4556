from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Flask backend is running!"

@app.route("/place-order", methods=["POST"])
def place_order():
    data = request.json
    if not data:
        return jsonify({"error": "No data provided"}), 400

    name = data.get("name")
    email = data.get("email")
    address = data.get("address")
    total_price = data.get("total_price")

    if not name or not email or not address:
        return jsonify({"error": "Missing fields"}), 400

    # Simulate saving order
    print(f"Order received: {data}")
    return jsonify({"message": "Order placed successfully!"})

if __name__ == "__main__":
    app.run(debug=True)
