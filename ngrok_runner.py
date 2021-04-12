import sys

from flask import Flask
from pyngrok import ngrok

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello World!"


if __name__ == "__main__":
    url = ngrok.connect(5000)
    print("\n" + "\033[96m {}\033[00m".format(url.public_url) + "\n")
    app.run()
