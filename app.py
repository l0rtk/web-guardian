from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("starter.html")


if "__main__" == __name__:
    app.run()
