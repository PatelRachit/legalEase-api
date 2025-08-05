from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app,resources={r"/*": {"origins": ["http://localhost:5173","https://legal-ease-frontend-henna.vercel.app"]}})

@app.route('/simplify', methods=['POST'])
def echo_text():
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    data = request.get_json()
    if 'text' not in data or not isinstance(data['text'], str):
        return jsonify({"error": "Missing or invalid 'text' field"}), 400

    input_text = data['text']
    return jsonify({"outputText": input_text})


if __name__ == '__main__':
    app.run(debug=True)
