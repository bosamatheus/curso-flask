from app import app


@app.route("/")
@app.route("/index")
def index():
    return "Hello!"

@app.route("/test", defaults={"name": None})
@app.route("/test/<name>")
def teste(name):
    if name:
        return "Hello, %s!" % name
    else:
        return "Hello!"
