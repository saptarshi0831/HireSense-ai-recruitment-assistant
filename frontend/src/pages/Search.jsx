import { useState } from "react";
import { searchCandidates } from "../services/api";
import CandidateCard from "../components/CandidateCard";

function Search() {
  const [query, setQuery] = useState("");
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);

  async function handleSearch() {
    setLoading(true);

    const res = await searchCandidates(query);

    setResults(res.results);

    setLoading(false);
  }

  return (
    <div>
      <h2>Search Candidates</h2>

      <input
        value={query}
        onChange={(e) => setQuery(e.target.value)}
      />

      <button onClick={handleSearch}>Search</button>

      {loading && <p>Searching...</p>}

      {results?.map((candidate, i) => (
        <CandidateCard key={i} candidate={candidate} />
      ))}
    </div>
  );
}

export default Search;