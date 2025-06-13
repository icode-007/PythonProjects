from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Titans - from Azure App Service!\n"

