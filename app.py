from flask import Flask,render_template,url_for,request

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "POST":
        keywords = request.form["keywords"].split(",")
        websites = request.form["websites"].split(",")

    return render_template("starter.html")


@app.route("/loading")
def loading():
    return render_template("spinner.html")

if "__main__" == __name__:
    app.run()
