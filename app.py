from flask import Flask, render_template as rt

web = Flask(__name__)

@web.route("/")
def home():
    return rt("index.html")

@web.route("/info")
def infomation():
    return rt("info.html")

@web.route("/rewards")
def rewards():
    return rt("rewards.html")

if __name__ == "__main__":
    web.run(debug=True)