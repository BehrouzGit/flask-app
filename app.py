from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask! This is the main branch."

@app.route("/about")
def about():
    return "Welcome to the About Page! - Contributed by Behrouz ACN"

@app.route("/contact")
def contact():
    return "Contact us at contact@example.com"



if __name__ == "__main__":
    app.run(debug=True)
