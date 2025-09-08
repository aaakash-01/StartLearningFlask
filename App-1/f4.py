from flask import Flask

app = Flask(__name__)

def name():
    return "hello Apsara kaisi hoo Aap"

app.add_url_rule("/name","name" ,name)

if __name__=="__main__":
    app.run(debug=True)