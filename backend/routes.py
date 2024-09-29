from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Willkommen zur Startseite!"

@app.route('/api/data', methods=['GET'])
def get_data():
    data = {
        'name': 'Beispiel',
        'value': 42
    }
    return jsonify(data)

@app.route('/api/data', methods=['POST'])
def post_data():
    new_data = request.json
    # Hier können Sie den Code hinzufügen, um die Daten zu speichern
    return jsonify(new_data), 201

if __name__ == '__main__':
    app.run(debug=True)