from flask import Flask, render_template

myapplication = Flask(__name__)


@myapplication.route("/")
def home_page():
    return render_template("index.html")

if __name__ == "__main__":
    myapplication.run(debug=True)
