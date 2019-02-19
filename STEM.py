from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/introduction")
def introduction():
    return render_template("introduction.html")


@app.route("/questions")
def questions():
    return render_template("questions.html")


@app.route("/answers")
def answers():
    return render_template("answers.html")


@app.route("/instructions")
def instructions():
    return render_template("instructions.html")


@app.route("/inbox")
def inbox():
    return render_template("inbox.html")


@app.route("/email1")
def email1():
    return render_template("email1.html")


@app.route("/email2")
def email2():
    return render_template("email2.html")


@app.route("/email3")
def email3():
    return render_template("email3.html")


@app.route("/email4")
def email4():
    return render_template("email4.html")


@app.route("/email5")
def email5():
    return render_template("email5.html")

@app.route("/results")
def results():
    return render_template("results.html")


@app.route("/resources")
def resources():
    return render_template("resources.html")

if __name__ == "__main__":
    app.run(debug=True)
