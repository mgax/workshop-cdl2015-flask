import flask

app = flask.Flask(__name__)


@app.route('/')
def home():
    return "Hello Flask!"


app.run(debug=True)
