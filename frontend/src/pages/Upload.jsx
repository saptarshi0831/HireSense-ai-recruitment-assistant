import { useState } from "react";
import { uploadResume } from "../services/api";

function Upload() {
  const [file, setFile] = useState(null);
  const [status, setStatus] = useState("");

  async function handleUpload() {
    if (!file) return;

    setStatus("Uploading...");

    const result = await uploadResume(file);

    setStatus(`Uploaded: ${result.filename}`);
  }

  return (
    <div>
      <h2>Upload Resume</h2>

      <input
        type="file"
        onChange={(e) => setFile(e.target.files[0])}
      />

      <br />
      <br />

      <button onClick={handleUpload}>Upload</button>

      <p>{status}</p>
    </div>
  );
}

export default Upload;