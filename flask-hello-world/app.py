# ---- Flask Hello World ---- #

from flask import Flask

app = Flask(__name__)

app.config["DEBUG"] = True


@app.route("/test/<search_query>")
def search(search_query):
    return search_query


@app.route("/")
@app.route("/hello")
def hello_world():
    return "Hello, World!?!?!?!"
if __name__ == "__main__":
    app.run()