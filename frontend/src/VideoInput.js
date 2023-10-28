import React from "react";
import axios from 'axios';

export default function VideoInput(props) {
  const { width, height } = props;

  const inputRef = React.useRef();

  const [source, setSource] = React.useState();

  const audio = true;

  const handleUpload = async (event) => {
    const file = event.target.files[0];
    const formData = new FormData();
    formData.append('video', file);
    
    try {
      await axios.post('http://localhost:5000/upload', formData, {
        headers: { 'Content-Type': 'multipart/form-data' },
      });
    } catch (error) {
      console.error('Error uploading video:', error);
    }
  };

  const handleChoose = (event) => {
    inputRef.current.click();
  };

  return (
    <div>
      <div className={source ? "VideoInputted" : "VideoInput"}>
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
      {/* {!source && <button onClick={handleChoose}>Choose</button>} */}
      {source && (
        <video
          className="VideoInput_video"
          width="100%"
          height={height}
          controls
          src={source}
        />
      )}
      <div className="VideoInput_footer">
        {audio ? (
          <div>
            <p>Audio has been generated!</p>
            <audio className="VideoInput_video" controls src={audio} />
          </div>
        ) : source ? (
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
