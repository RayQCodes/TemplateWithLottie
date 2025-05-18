from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/second")
def second():
    return render_template("index2.html")



if __name__ == "__main__":
    app.run(debug=True)