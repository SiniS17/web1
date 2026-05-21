from flask import Flask, render_template


app = Flask(__name__)
print(__name__)


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/rules')
def rules():
    return render_template("rules.html")

@app.route('/hotspot')
def hotspot():
    return render_template("hotspot.html")

@app.route('/tools')
def b787_tools():
    return render_template("b787_tools.html")

if __name__ == "__main__":
    app.run(debug=True)