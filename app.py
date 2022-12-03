from flask import Flask, render_template, request
from models.load_json import User

app = Flask(__name__)

@app.route("/")
def home():
    data = User("data/score.json")
    name = data.users
    length = len(name)
    scores = data.scores
    return render_template("home.html", name = name, length = length)


@app.route("/player")
def get_name():
    data = User("data/score.json")
    name = data.users
    length = len(name)
    uname = request.args.get('player')
    return render_template("one_player.html", name = name, uname=uname, length = length )



if __name__ == "__main__":
    app.run(debug=True, port = 5000)