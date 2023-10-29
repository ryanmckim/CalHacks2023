import os
from flask import Flask, send_from_directory, request
from flask_cors import cross_origin

app = Flask(__name__)

video_audio_mapping = {
    "nature_img.jpg": "nature_img.wav",
    "party.mp4": "party.wav",
    "xmas.mp4": "xmas.wav"
}

# Socket IO connection

# def generate_audio():
#     audio_data = "data"
#     yield f"data: {audio_data}\n\n"

# @app.route('/get_audio_stream')
# def get_audio_stream():
#     return Response(generate_audio(), content_type="text/event-stream")

@app.route("/get_audio/<filename>")
@cross_origin()
def get_audio(filename):
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