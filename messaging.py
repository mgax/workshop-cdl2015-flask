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
    flask.flash("Message '%s' saved" % text)
    return flask.redirect(flask.url_for('home'))


@app.route('/message/<int:message_id>')
def message_view(message_id):
    message = Message.query.get_or_404(message_id)
    return flask.render_template('message.html', message=message)


@app.route('/message/<int:message_id>/delete')
def message_delete(message_id):
    message = Message.query.get_or_404(message_id)
    return flask.render_template('delete.html', message=message)


db.create_all()
app.run(debug=True)
