from flask import Flask, request, jsonify

app = Flask(__name__)

database = []

@app.route('/submit-data', methods=['POST'])
def submit_data():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid data"}), 400

    database.append(data)
    print("Received data:", data)

    return jsonify({"message": "Data received successfully", "data": data}), 200

if __name__ == '__main__':
    app.run(debug=True)
