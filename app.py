from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask! This is the main branch."

if __name__ == "__main__":
    app.run(debug=True)
