from flask import Flask, render_template
from views.blog import blog
from views.user import user

app = Flask(__name__)

app.register_blueprint(blog, url_prefix='/blog')
app.register_blueprint(user, url_prefix='/user')


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
