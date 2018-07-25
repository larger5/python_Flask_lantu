from flask import Blueprint, render_template

blog = Blueprint('blog', __name__, template_folder='../templates/blog')


@blog.route('/index/')
def index():
    return render_template('blog.html')


@blog.route('/welcome/')
def welcome():
    return "welcome to blog"
