from flask import Flask

app = Flask(__name__)

@app.route('/name/<int:age>')
def name(age):
    return "Age = %d" %age

if __name__=="__main__":
    app.run(debug=True)