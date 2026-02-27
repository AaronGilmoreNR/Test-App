from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello, Azure!</h1><p>My web app is officially running in the cloud.</p>"

if __name__ == "__main__":
    app.run()
