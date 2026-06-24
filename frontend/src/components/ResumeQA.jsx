import { useState } from "react";
import axios from "axios";
import ReactMarkdown from "react-markdown";

import "../styles/qa.css";

function ResumeQA() {
  const [query, setQuery] = useState("");
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] = useState(false);

  async function askQuestion() {
    if (!query.trim()) return;

    try {
      setLoading(true);
      setAnswer("");

      const res = await axios.get(
        "http://127.0.0.1:8000/resume-qa",
        {
          params: { query }
        }
      );

      setAnswer(res.data.answer);
    } catch {
      setAnswer("Unable to generate response.");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="qa-container">
      <h2 className="qa-title">Recruiter Assistant</h2>

      <p className="tagline">
        Ask questions about uploaded resumes.
      </p>

      <div className="form-row">
        <input
          value={query}
          className="input"
          placeholder="Who worked on RAG?"
          onChange={(e) => setQuery(e.target.value)}
          onKeyDown={(e) => {
            if (e.key === "Enter") {
              askQuestion();
            }
          }}
        />

        <button
          onClick={askQuestion}
          disabled={loading}
        >
          {loading ? "Thinking..." : "Ask"}
        </button>
      </div>

      {!answer && !loading && (
        <div className="qa-placeholder">
          Try:
          <br />
          • Who worked on RAG?
          <br />
          • Which candidate has backend experience?
          <br />
          • Strongest AI project?
        </div>
      )}

      {answer && (
        <div className="qa-answer">
          <ReactMarkdown>{answer}</ReactMarkdown>
        </div>
      )}
    </div>
  );
}

export default ResumeQA;