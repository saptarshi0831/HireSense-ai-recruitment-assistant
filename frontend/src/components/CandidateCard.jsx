import "../styles/card.css";

function CandidateCard({ candidate }) {
return (
<div className="card">

<div className="card-top">

<div>

<h2 className="candidate-name">
{candidate.candidate || "Unknown Candidate"}
</h2>

<p className="candidate-summary">
{candidate.summary || "No summary available"}
</p>

</div>

<div className="card-metrics">

<div className="badge score">
Match<br/>
{candidate.match_score}%
</div>

<div className={`badge confidence ${candidate.confidence?.toLowerCase()}`}>
{candidate.confidence || "Medium"}
</div>

</div>

</div>

<h4>Skills</h4>

<div className="skills">
{candidate.skills?.length ? (
candidate.skills.map((skill,index)=>(
<span key={index} className="skill">
{skill}
</span>
))
) : (
<span className="empty">Not detected</span>
)}
</div>

<div className="warning">
AI recommendations may be imperfect. Review resume before decisions.
</div>

<a
className="resume-btn"
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