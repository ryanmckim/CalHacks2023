import NavBar from "../components/NavBar";
import Button from "../components/Button";
import divider from "../imgs/divider.svg";
import { NavLink } from "react-router-dom";

const Home = () => {
  return (
    <>
      <NavBar />
      <main className="homeContent">
        <div className="homeText">
          <span className="gradientFont">YOUR CONTENT, </span>
          <br />
          <span className="gradientFont"> YOUR SOUNDTRACK. </span>
          <br />
          <p>
          The new sound of music, at the tip of your fingers. 
          Effortlessly create custom music from your content with speed and personalization.
          </p>
            <NavLink className= "btn-primary" to="/demo">Get Started</NavLink>
        </div>
        <img alt="divider" className="divider" src={divider} />
      </main>
    </>
  );
};

export default Home;
