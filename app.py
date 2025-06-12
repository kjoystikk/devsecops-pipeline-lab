from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, DevSecOps!"



import os

if __name__ == "__main__":
    if os.environ.get("CI"):
        app.run(host="127.0.0.1", port=5000)  # безопасный запуск для CI
    else:
        app.run(host="0.0.0.0", port=5000)    # для dev/docker
