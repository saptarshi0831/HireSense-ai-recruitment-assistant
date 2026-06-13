import Upload from "./pages/Upload";
import Search from "./pages/Search";

function App() {
  return (
    <div style={{ maxWidth: "1000px", margin: "auto", padding: "30px" }}>
      <h1>AI Recruitment Assistant</h1>
      <hr />
      <Upload />
      <hr />
      <Search />
    </div>
  );
}

export default App;