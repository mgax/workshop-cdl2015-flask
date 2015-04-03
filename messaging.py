import flask

app = flask.Flask(__name__)


@app.route('/')
def home():
    return flask.render_template('home.html')


@app.route('/new', methods=['POST'])
def new():
    text = flask.request.form['message']
    print text
    return flask.redirect(flask.url_for('home'))


app.run(debug=True)
