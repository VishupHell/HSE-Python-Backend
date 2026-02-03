from flask import Flask
from flask import jsonify
from dotenv import dotenv_values

app = Flask(__name__)

@app.route("/author")
def author():
    author = {
        "name": "Torosyan Andranik",
        "course": 2,
        "age": 19,
    }
    return jsonify(author)

@app.route("/")
def server_info():
    return "My first flask server"

def get_port():
    config = dotenv_values(".env")
    if "PORT" in config:
        return config["PORT"]
    return 5000

if __name__ == "__main__":
    app.run(debug=True, port=get_port())