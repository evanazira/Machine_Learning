from flask import Flask
app = Flask(__name__)

@app.route("/")
def say_hello():
    return "Hello World!!!"

# @app.route("product")
# def get_product()
int()