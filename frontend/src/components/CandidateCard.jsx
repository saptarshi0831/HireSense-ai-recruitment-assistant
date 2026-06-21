function CandidateCard({ candidate }) {
  return (
    <div
      style={{
        border: "1px solid #ddd",
        borderRadius: "10px",
        padding: "20px",
        marginBottom: "20px",
      }}
    >
      <h2>{candidate.candidate}</h2>

      <p>
        Skills:{" "}
        {candidate.skills?.length
          ? candidate.skills.join(", ")
          : "Not detected"}
      </p>

      <p>Summary: { candidate.summary || "No summary available"} </p>

      <p>Match Score: {candidate.match_score}%</p>

      <p>
        Retrieval Confidence:{" "}
        <span
          style={{
            color:
              {
                High: "green",
                Medium: "orange",
              }[candidate.confidence] || "red",
            fontWeight: "bold",
          }}
        >
          {candidate.confidence}
        </span>
      </p>

      <p
        style={{
          fontSize: "12px",
          color: "red",
        }}
      >
        Results may be imperfect. Review resume before decisions.
      </p>

      <a
        href={`http://127.0.0.1:8000/resume/${candidate.filename}`}
        target="_blank"
        rel="noopener noreferrer"
      >
        View Resume
      </a>
    </div>
  );
}

export default CandidateCard;