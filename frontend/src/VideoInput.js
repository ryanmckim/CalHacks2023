import React from "react";
import axios from "axios";

export default function VideoInput(props) {
  const temp = new Map();
  temp.set("nature.mp4", "nature.wav");
  temp.set("party.mp4", "party.wav");
  temp.set("volleyball.mp4", "volleyball.wav");

  const { width, height } = props;
  const inputRef = React.useRef();
  const [video, setVideo] = React.useState();
  const [audio, setAudio] = React.useState();

  const handleUpload = async (event) => {
    const file = event.target.files[0];
    const fileName = file.name;
    const videoURL = URL.createObjectURL(file);
    setVideo(videoURL);
    const formData = new FormData();
    formData.append('video', file);

    await axios.post("http://localhost:5000/upload", formData, {
        headers: { "Content-Type": "multipart/form-data" },
    });

    try {
      await axios.post(`http://localhost:5000/upload/${fileName}`, formData, {
          headers: { "Content-Type": "multipart/form-data" },
      });
    } catch (error) {
      console.log(error)
    }

    const response = await axios.get(`http://localhost:5000/get_audio/${fileName}`, {
      responseType: 'blob'
    });

    const audioBlob = response.data;
    const audioURL = URL.createObjectURL(audioBlob);
    setAudio(audioURL);
  };

  return (
    <div>
      <div className={video ? "VideoInputted" : "VideoInput"}>
        <label for="vidInput">Browse Files</label>

        <input
          id="vidInput"
          ref={inputRef}
          className="VideoInput_input"
          type="file"
          onChange={handleUpload}
          accept=".mov,.mp4"
        />
      </div>
      {video && (
        <video
          className="VideoInput_video"
          width="100%"
          height={height}
          controls
          src={video}
        />
      )}
      <div className="VideoInput_footer">
        {audio ? (
          <div style={{ width: "100%" }}>
            <p>Audio has been generated!</p>
            <audio className="VideoInput_video" controls src={audio} />
          </div>
        ) : audio ? (
          <div className="center">
            <div className="lds-ripple">
              <div></div>
              <div></div>
            </div>
            <p>Generating audio file...</p>
          </div>
        ) : (
          <p>Upload a video to generate audio</p>
        )}
      </div>
    </div>
  );
}
