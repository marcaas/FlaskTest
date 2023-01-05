from flask import Flask

app = Flask(__name__)


# url：http[80]/https[443]://www.qq.com:443/path
# url与视图：path与视图

@app.route('/')
def hello_world():
    return 'Hello world!'


@app.route("/profile")
def profile():
    return "我是个人中心！"


@app.route("/blog/list")
def blog_list():
    return "这是博客列表。"
    

if __name__ == '__main__':
    app.run(debug=True)