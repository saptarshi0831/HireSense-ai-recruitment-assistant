import { useState } from "react";

import Search from "../pages/Search";
import ResumeQA from "./ResumeQA";
import CandidateCompare from "./CandidateCompare";

import "../styles/tabs.css";

function Tabs() {
  const [tab, setTab] = useState("search");

  return (
    <div className="tabs-wrapper">

      <div className="tabs">

        <button
          className={`tab ${tab === "search" ? "active" : ""}`}
          onClick={() => setTab("search")}
        >
          Search
        </button>

        <button
          className={`tab ${tab === "qa" ? "active" : ""}`}
          onClick={() => setTab("qa")}
        >
          Recruiter Assistant
        </button>

        <button
          className={`tab ${tab === "compare" ? "active" : ""}`}
          onClick={() => setTab("compare")}
        >
          Compare
        </button>

      </div>

      <div className="tab-content">

        {tab === "search" && <Search />}
        {tab === "qa" && <ResumeQA />}
        {tab === "compare" && <CandidateCompare />}

      </div>

    </div>
  );
}

export default Tabs;