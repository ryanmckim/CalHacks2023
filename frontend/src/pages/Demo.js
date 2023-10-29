import NavBar from "../components/NavBar";
import VideoInput from "../VideoInput";

const Demo = () => {
  return (
    <>
      <NavBar />
      <main className="demoContent">
        <div className="videoUpload">
          <h1>Upload Your Content</h1>
          <VideoInput width={500} height={400} />
        </div>
        <div className="demoText">
        </div>
      </main>
    </>
  );
};

export default Demo;
