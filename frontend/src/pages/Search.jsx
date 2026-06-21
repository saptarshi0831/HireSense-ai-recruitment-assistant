import { useState } from "react";
import { searchCandidates } from "../services/api";
import CandidateCard from "../components/CandidateCard";

function Search() {
  const [query, setQuery] = useState("");
  const [results, setResults] = useState([]);
  const [searched, setSearched] = useState(false);
  const [loading, setLoading] = useState(false);

  async function handleSearch() {
    setLoading(true);
    setResults([]);

    try {
      const res = await searchCandidates(query);

      setSearched(true);
      setResults(res.results);
    } finally {
      setLoading(false);
    }
  }

  return (
    <div>
      <h2>Search Candidates</h2>

      <input
        value={query}
        onChange={(e) => setQuery(e.target.value)}
      />

      <button onClick={handleSearch} disabled={loading}>
        {loading ? "Searching..." : "Search"}
      </button>

      {loading && <p>Loading...</p>}

      {searched && !loading && results.length === 0 && (
        <p>No matching candidates</p>
      )}

      {results.map((candidate, i) => (
        <CandidateCard
          key={i}
          candidate={candidate}
        />
      ))}
    </div>
  );
}

export default Search;