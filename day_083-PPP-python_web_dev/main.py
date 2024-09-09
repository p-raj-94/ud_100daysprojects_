from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from dotenv import load_dotenv
from markupsafe import escape
import os
from flask import json




load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("FLASK_KEY")
Bootstrap5(app)
app.debug = False

with open("static/data.json") as f:
    data = json.load(f)

@app.route("/")
def home():
    jobs = data["jobs"]
    diplomes = data["diplomes"]
    return render_template("index.html", jobs= jobs, diplomes=diplomes)

if __name__ == "__main__":
    app.run(debug=False)