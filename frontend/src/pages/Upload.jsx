import { useState } from "react";
import { uploadResumes } from "../services/api";

function Upload() {
  const [file, setFile] = useState(null);
  const [status, setStatus] = useState("");

  async function handleUpload() {
    if (!file) return;
  
    setStatus("Uploading...");
  
    try {
      const result = await uploadResumes(file);
    
      console.log("Result:", result);
    
      setStatus(`Processed: ${result.processed}`);
    } catch (err) {
      console.error(err);
      setStatus("Upload failed");
    }
  }

  return (
    <div>
      <h2>Upload Resume</h2>

      <input
        type="file"
        accept=".zip"
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