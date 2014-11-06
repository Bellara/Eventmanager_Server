__author__ = 'Henning'

from flask import Flask
app = Flask(__name__)

@app.route("/Test")
def hello():
    return "Test erfolgreich!"

if __name__ == "__main__":
    app.run()
