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

      <p>Match: {candidate.match_score}%</p>

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