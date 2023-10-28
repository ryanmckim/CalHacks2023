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
          <span className="gradientFont">CATCH PHRASE. </span>
          <br />
          <span className="gradientFont"> GOES HERE. </span>
          <br />
          <p>
            Gorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc
            vulputate libero et velit interdum, ac aliquet odio mattis. Class
            aptent taciti sociosqu ad litora torquent per conubia nostra, per
            inceptos himenaeos. Curabitur tempus urna at turpis condimentum
            lobortis.
          </p>
            <NavLink className= "btn-primary" to="/demo">Get Started</NavLink>
        </div>
        <img alt="divider" className="divider" src={divider} />
      </main>
    </>
  );
};

export default Home;
