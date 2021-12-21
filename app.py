from flask import Flask,render_template,url_for,request,redirect
from flask_restful import Resource, Api,reqparse

app = Flask(__name__)
api = Api(app)


parser = reqparse.RequestParser()
parser.add_argument('keywords')
parser.add_argument('websites')





@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "POST":
        keywords = request.form["keywords"]
        websites = request.form["websites"]
        return redirect(url_for("loading",keywords=keywords,websites=websites))
    return render_template("starter.html")


@app.route("/loading", methods=["GET","POST"])
def loading():
    keywords = request.args["keywords"]
    websites = request.args["websites"]

    return render_template("spinner.html",keywords = keywords,websites = websites)


class Sentences(Resource):
    def get(self):
        return {'hello': 'world'}


    def post(self):
        args = parser.parse_args()

        keywords = args["keywords"].split(',')
        websites = args["websites"].split(',')

        return {"fuck" : "YOU"}





api.add_resource(Sentences, '/hello_world')


if "__main__" == __name__:
    app.run()
