from flask import Flask, render_template

app = Flask("website")

@app.route("/")
def home():
    pass

@app.route("/api/<station>/<date>")
def about():
    pass

app.run(debug=True)