import React from "react";

export default function VideoInput(props) {
  const { width, height } = props;

  const inputRef = React.useRef();

  const [source, setSource] = React.useState();

  const audio = null;

  const handleFileChange = (event) => {
    const file = event.target.files[0];
    const url = URL.createObjectURL(file);
    setSource(url);
  };

  const handleChoose = (event) => {
    inputRef.current.click();
  };

  return (
    <div className="VideoInput">
      <input
        ref={inputRef}
        className="VideoInput_input"
        type="file"
        onChange={handleFileChange}
        accept=".mov,.mp4"
      />
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
      {audio && <audio className="VideoInput_video" controls src={audio} />}
      <div className="VideoInput_footer">
        {audio ? <p>Audio has been generated!</p> : <p></p>}
      </div>
    </div>
  );
}
