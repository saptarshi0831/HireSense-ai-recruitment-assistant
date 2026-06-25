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

      await axios.post(
        "http://127.0.0.1:8000/upload-resume",
        form
      );

      setUploaded(file.name);
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
            Drag & drop ZIP files or click to upload resumes
          </div>

          <div className="upload-hint">
            Supports .zip and .pdf
          </div>
        </div>
      </label>

      {loading && (
        <div className="upload-loading">
          Uploading resumes...
        </div>
      )}

      {uploaded && (
        <div className="upload-success">
          ✓ Uploaded: {uploaded}
        </div>
      )}
    </div>
  );
}

export default UploadResume;