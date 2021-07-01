from flask import Blueprint, render_template, redirect, url_for, session

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return redirect(url_for('main.home'))


@main.route('/home')
def home():
    return render_template('home.html', modal_event=session.pop('modal_event', None))
