from flask import Flask, redirect, url_for, session

from .main import main as main_blueprint

from .constants import EVENT_404

app = Flask(__name__)

# Generate secret key = import os >>> os.urandom(24)
app.config['SECRET_KEY'] = '\xb1\x17Y\x01P\xfc\xb8\xb4\xb6\xa4\xdd\xc2,C!\x06\x8b\x96\xb8\xc5\xfa\xfcQ\xe2'

# blueprints for non-auth parts of app
app.register_blueprint(main_blueprint)


@app.errorhandler(404)
# inbuilt function which takes error as parameter
def not_found(e):
    session['modal_event'] = EVENT_404
    return redirect(url_for('main.home'))
