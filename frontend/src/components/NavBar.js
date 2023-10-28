import { NavLink } from "react-router-dom";
import navbarLogo from "../imgs/Union.svg";

const NavBar = () => {
  return (
    <nav className="navbar">
      <div className="navbar-logo">
        <NavLink to="/">
          <img
            alt="logo"
            src={navbarLogo}
            width="50"
          />
          <p>ProductName</p>
        </NavLink>
      </div>
      <div className="navbar-links">
        <NavLink to="/demo">Demo</NavLink>
      </div>
    </nav>
  );
};

export default NavBar;