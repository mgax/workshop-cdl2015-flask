import flask

app = flask.Flask(__name__)


@app.route('/')
def home():
    return flask.render_template('home.html')


app.run(debug=True)
