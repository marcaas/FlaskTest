
@app.route('/filter')
def hello_world():
    user = User(username="marcaas", email="marcaas@china.com")
    return render_template("filter.html", user=user)