import "./App.css";
import { Routes, Route } from "react-router-dom";
import Home from "./pages/Home";
import Demo from "./pages/Demo";

export default function App() {

  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/demo" element={<Demo />} />
      <Route
        path="*"
        element={
          <main className="page-not-found">
            <p>Page not found</p>
          </main>
        }
      />
    </Routes>
  );
}
