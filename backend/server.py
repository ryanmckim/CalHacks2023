from flask import Flask

app = Flask(__name__)

@app.route("/members")

def test():
    return {"members": ["hello", "bye"]}

if __name__ == "__main__":
    app.run(debug=True)