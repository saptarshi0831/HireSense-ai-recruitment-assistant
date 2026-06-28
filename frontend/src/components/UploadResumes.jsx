import { useState } from "react";
import axios from "axios";

import "../styles/upload.css";

function UploadResume() {
  const [loading, setLoading] = useState(false);
  const [uploaded, setUploaded] = useState("");

  async function upload(e) {
    const file = e.target.files[0];

    if (!file) return;

    try {
      setLoading(true);
      setUploaded("");

      const form = new FormData();
      form.append("file", file);

      const res = await axios.post(
        "http://127.0.0.1:8000/upload-resumes",
        form
      );

      setUploaded(
        `Successfully uploaded "${file.name}". Parsed and indexed ${res.data.processed} resumes. Ready for AI search.`
      );
    } catch (err) {
      console.error(err);

      setUploaded(
        "Upload failed. Please try again."
      );
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="upload-box">
      <label>
        <input
          hidden
          type="file"
          accept=".zip,.pdf"
          onChange={upload}
        />

        <div className="upload-card">
          <div className="upload-icon">
            📂
          </div>

          <div className="upload-title">
            Upload Resume Database
          </div>

          <div className="upload-text">
            Upload a ZIP file containing multiple resumes or a single PDF.
          </div>

          <div className="upload-hint">
            Supported formats: .zip, .pdf
          </div>
        </div>
      </label>

      {loading && (
        <div className="upload-loading">
          ⏳ Uploading, parsing, generating embeddings, and indexing resumes...
        </div>
      )}

      {uploaded && (
        <div className="upload-success">
          {uploaded}
        </div>
      )}
    </div>
  );
}

export default UploadResume;