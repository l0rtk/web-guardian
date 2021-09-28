from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World"



if "__main__" == __name__:
    app.run()