from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("starter.html")


@app.route("/loading")
def loading():
    return render_template("spinner.html")

if "__main__" == __name__:
    app.run()
