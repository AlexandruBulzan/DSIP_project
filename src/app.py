# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, this is your app running inside a Docker container!"

if __name__ == "__main__":
    # This is where you specify the host and port
    app.run(host="0.0.0.0", port=8080)


