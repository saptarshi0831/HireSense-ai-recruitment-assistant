import Tabs from "./components/Tabs";
import "./styles/app.css";

function App() {
  return (

    <div className="page">

      <div className="container">

        <section className="hero">

          <h1 className="page-title">

            HireSense

          </h1>

          <p className="tagline">

            Intelligent Resume Screening • Faster Hiring • Better Decisions

          </p>

        </section>


        <main className="content">

          <Tabs />

        </main>

      </div>


      <footer className="footer">

        AI-generated recommendations may contain inaccuracies.

      </footer>

    </div>

  );
}

export default App;