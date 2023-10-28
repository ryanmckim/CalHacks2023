import NavBar from "../components/NavBar";
import Footer from "../components/Footer";
import VideoInput from "../VideoInput";

const Demo = () => {
  return (
    <>
      <NavBar />
      <main className="demoContent">
        <div className="videoUpload">
          <h1>Upload Your Video</h1>
          <VideoInput width={400} height={300} />
        </div>
        <div className="demoText">
        </div>
      </main>
      <Footer />
    </>
  );
};

export default Demo;
