import { useState } from "react";
import { searchCandidates } from "../services/api";
import CandidateCard from "../components/CandidateCard";

import "../styles/search.css";

function Search() {
  const [query, setQuery] = useState("");
  const [results, setResults] = useState([]);
  const [searched, setSearched] = useState(false);
  const [loading, setLoading] = useState(false);

  async function handleSearch() {
    if (!query.trim()) return;

    setLoading(true);
    setResults([]);

    try {
      const res = await searchCandidates(query);

      setSearched(true);
      setResults(res.results || []);
    } catch {
      setResults([]);
    } finally {
      setLoading(false);
    }
  }

  return (
    <section className="search-section">
      <div className="search-header">
        <h2>Search Candidates</h2>

        <p>
          Find the most relevant candidates instantly using AI.
        </p>
      </div>

      <div className="search-box">
        <div className="form-row">
          <input
            type="text"
            placeholder="Enter skills, role, or keywords..."
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            onKeyDown={(e) => {
              if (e.key === "Enter") {
                handleSearch();
              }
            }}
          />

          <button onClick={handleSearch} disabled={loading}>
            {loading ? "Searching..." : "Search"}
          </button>
        </div>
      </div>

      {loading && (
        <div className="loader">
          Searching resumes...
        </div>
      )}

      {searched && !loading && results.length === 0 && (
        <div className="empty-state">
          <h3>No matching candidates</h3>

          <p>
            Try:
            <span> Python backend developer </span>
          </p>
        </div>
      )}

      {results.length > 0 && (
        <div className="results-grid">
          {results.map((candidate, i) => (
            <CandidateCard
              key={i}
              candidate={candidate}
            />
          ))}
        </div>
      )}
    </section>
  );
}

export default Search;