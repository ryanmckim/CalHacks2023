import os
from flask import Flask, send_from_directory, request, jsonify
from flask_cors import cross_origin
from audio_generation.gen_model import main as generate_audio_from_media

app = Flask(__name__, static_folder='../build', static_url_path='/')

video_audio_mapping = {
    "nature_img.jpg": "nature_img.wav",
    "party.mp4": "party.wav",
    "xmas.mp4": "xmas.wav"
}

UPLOAD_FOLDER = 'uploads'
AUDIO_FOLDER = 'audio'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(AUDIO_FOLDER, exist_ok=True)


def save_uploaded_file(file, folder):
    filename = file.filename
    file_path = os.path.join(folder, filename)
    file.save(file_path)
    return filename, file_path

def generate_audio(file_path):
    """Generate audio from the media file."""
    audio_filename = os.path.splitext(os.path.basename(file_path))[0] + '.wav'
    audio_path = os.path.join(AUDIO_FOLDER, audio_filename)
    generate_audio_from_media(file_path, audio_path)
    return audio_filename

# Socket IO connection

#@app.route('/get_audio_stream')
#def get_audio_stream():
#    return Response(generate_audio(), content_type="text/event-stream")

@app.route("/get_audio/<filename>", methods=['GET'])
@cross_origin()
def get_audio(filename):
    """GET: Get the audio file."""
    return send_from_directory(AUDIO_FOLDER, filename, as_attachment=True)

@app.route("/upload", methods=['POST'])
@cross_origin()
def upload_file():
    """POST: Handles file uploads."""
    
    if request.method != 'POST':
        return '', 204  # No Content status code
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    try:
        filename, file_path = save_uploaded_file(file, UPLOAD_FOLDER)
        generate_audio(file_path)
        return jsonify({"success": True}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/')
def list_endpoints():
    """Lists all defined endpoints and descriptions."""
    endpoints = {}
    for rule in app.url_map.iter_rules():
        if rule.endpoint != 'static':
            endpoint = app.view_functions[rule.endpoint]
            docstring = endpoint.__doc__ if endpoint.__doc__ else "No description available."
            endpoints[rule.rule] = docstring.strip()
    return jsonify(endpoints)


if __name__ == "__main__":
    app.run(debug=True)
