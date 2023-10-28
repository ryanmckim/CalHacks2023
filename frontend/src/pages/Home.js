import NavBar from "../components/NavBar";
import Footer from "../components/Footer";
import Button from "../components/Button";
const Home = () => {

return (
    <>
    <NavBar />
    <main className="homeContent">
        <div className="homeText">
            <p>test home</p>
            <Button onClick={null}>Test</Button>
        </div>
    </main>
    <Footer />
    </>
);
};

export default Home;