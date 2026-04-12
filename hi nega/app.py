from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/dress1')
def dress1():
    return render_template("dress1.html")


@app.route('/dress2')
def dress2():
    return render_template("dress2.html")


@app.route('/dress3')
def dress3():
    return render_template("dress3.html")


@app.route('/dress4')
def dress4():
    return render_template("dress4.html")


@app.route('/dress5')
def dress5():
    return render_template("dress5.html")


@app.route('/dress6')
def dress6():
    return render_template("dress6.html")


@app.route('/dress7')
def dress7():
    return render_template("dress7.html")


if __name__ == "__main__":
    app.run(debug=True)
