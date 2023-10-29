import os
from flask import Flask, send_from_directory, request
from flask_cors import cross_origin

app = Flask(__name__)

video_audio_mapping = {
    "nature.mp4": "nature.wav",
    "party.mp4": "party.wav",
    "volleyball.mp4": "volleyball.wav"
}

@app.route("/get_audio/<filename>")
@cross_origin()
def get_audio(filename):
    print("hello")
    print(video_audio_mapping.get(filename))
    print("hello")
    return send_from_directory("./audio/", video_audio_mapping.get(filename))

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