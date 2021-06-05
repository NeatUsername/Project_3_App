from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/index.html")
def index():
    return render_template("index.html")

@app.route("/dataset.html")
def dataset():
    return render_template("dataset.html")

@app.route("/analysis.html")
def Analysis():
    return render_template("analysis.html")

@app.route("/regression.html")
def regression():
    return render_template("regression.html")
    
if __name__ == "__main__":
    app.run(debug=True)