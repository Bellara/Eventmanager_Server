__author__ = 'Henning'

from flask import Flask
app = Flask(__name__)

@app.route("/Test")
def hello():
    return "Test erfolgreich!"

@app.route("/Test2")
def test_t():
    return "Zweiter Test!"

if __name__ == "__main__":
    app.run()
