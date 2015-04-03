import flask
from flask.ext.sqlalchemy import SQLAlchemy

app = flask.Flask(__name__)
app.config.from_pyfile('settings.py')
db = SQLAlchemy(app)


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String)


@app.route('/')
def home():
    messages = Message.query.all()
    return flask.render_template('home.html', messages=messages)


@app.route('/new', methods=['POST'])
def new():
    text = flask.request.form['message']
    message = Message(text=text)
    db.session.add(message)
    db.session.commit()
    return flask.redirect(flask.url_for('home'))


db.create_all()
app.run(debug=True)
