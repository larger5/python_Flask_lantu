from flask import Blueprint, render_template

user = Blueprint('user', __name__, template_folder='../templates')


@user.route('/index/')
def index():
    return render_template('user/user.html')


@user.route('/welcome/')
def welcome():
    return "welcome to user"
