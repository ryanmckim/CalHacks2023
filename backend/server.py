from flask import Flask
from flask_cors import cross_origin

app = Flask(__name__)

@app.route("/members")
@cross_origin()
def test():
    return ["hello", "bye"]

if __name__ == "__main__":
    app.run(debug=True)