import os
from flask import Flask, send_from_directory, request
from flask_cors import cross_origin

if not os.path.exists("./audio"):
    os.makedirs("./audio")

if not os.path.exists("./video"):
    os.makedirs("./video")

app = Flask(__name__)

@app.route("/get_audio/<filename>")
@cross_origin()
def get_audio(filename):
    return send_from_directory("./audio/", filename)

@app.route("/upload", methods=['POST'])
@cross_origin()
def upload_video():
    video = request.files['video']
    if video:
        file_path = "./video/" + video.filename
        video.save(file_path)
        # send file path to ML model
        return "Upload successful!"
    return "Upload unsuccessful."

if __name__ == "__main__":
    app.run(debug=True)