from flask import Flask

pflege_app = Flask(__name__)

if __name__ == '__main__':
    pflege_app.run(debug=True, host='0.0.0.0', port=5000)  # Host und Port hinzugefügt
