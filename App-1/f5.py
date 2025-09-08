from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hey():
    list_of_courses = ["C++", "DSA", "Java", "Python"]
    return render_template("ak.html", courses=list_of_courses)

if __name__ == "__main__":
    app.run(debug=True)
