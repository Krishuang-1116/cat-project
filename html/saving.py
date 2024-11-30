from flask import Flask, request, jsonify

app = Flask(__name__)

# 模拟数据库
database = []

@app.route('/submit-data', methods=['POST'])
def submit_data():
    data = request.get_json()  # 获取 JSON 数据
    if not data:
        return jsonify({"error": "Invalid data"}), 400

    # 将数据保存到数据库（这里是内存中）
    database.append(data)
    print("Received data:", data)

    return jsonify({"message": "Data received successfully", "data": data}), 200

if __name__ == '__main__':
    app.run(debug=True)
