from flask import Flask,render_template,url_for,request,redirect

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "POST":
        keywords = request.form["keywords"].split(",")
        websites = request.form["websites"].split(",")
        print(keywords)
        return redirect(url_for("loading",keywords=keywords,websites=websites))
    return render_template("starter.html")


@app.route("/loading", methods=["GET","POST"])
def loading():
    keywords = request.args
    websites = request.args

    print(request.args["keywords"])
    return render_template("spinner.html")

if "__main__" == __name__:
    app.run()
