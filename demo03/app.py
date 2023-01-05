from flask import Flask, render_template


app = Flask(__name__)


class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email


@app.route('/')
def hello_world():
    user = User(username="marcaas", email="marcaas@china.com")
    person = {
        "username": "zhangsan",
        "email": "zhangsan@qq.com"
    }
    return render_template("index.html", user=user, person = person)


@app.route('/blog/<blog_id>')
def blog_detail(blog_id):
    return render_template("blog_detail.html", blog_id=blog_id, username="marcaas")


@app.route('/filter')
def filter():
    user = User(username="marcaas", email="marcaas@china.com")
    return render_template("filter.html", user=user)


if __name__ == '__main__':
    app.run(debug=True)
