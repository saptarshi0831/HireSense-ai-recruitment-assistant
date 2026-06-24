import { useState } from "react";
import axios from "axios";
import ReactMarkdown from "react-markdown";

import "../styles/compare.css";

function CandidateCompare() {
  const [query, setQuery] = useState("");
  const [comparison, setComparison] = useState("");
  const [loading, setLoading] = useState(false);

  async function compareCandidates() {
    if (!query.trim()) return;

    try {
      setLoading(true);
      setComparison("");

      const res = await axios.get(
        "http://127.0.0.1:8000/compare",
        {
          params: { query }
        }
      );

      setComparison(res.data.comparison);
    } catch {
      setComparison("Unable to compare candidates.");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="compare-container">
      <h2 className="compare-title">Candidate Compare</h2>

      <p className="compare-subtitle">
        Compare candidates using skills, projects and resume evidence.
      </p>

      <div className="form-row">
        <input
          className="input"
          value={query}
          placeholder="compare python and golang candidates"
          onChange={(e) => setQuery(e.target.value)}
          onKeyDown={(e) => {
            if (e.key === "Enter") {
              compareCandidates();
            }
          }}
        />

        <button onClick={compareCandidates} disabled={loading}>
          {loading ? "Comparing..." : "Compare"}
        </button>
      </div>

      {!comparison && !loading && (
        <div className="compare-placeholder">
          Try:
          <br />
          • compare python and golang candidates
          <br />
          • compare backend candidates
          <br />
          • compare rag candidates
        </div>
      )}

      {comparison && (
        <div className="compare-output">
          <ReactMarkdown>{comparison}</ReactMarkdown>
        </div>
      )}
    </div>
  );
}

export default CandidateCompare;