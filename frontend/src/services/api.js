const BASE = "http://127.0.0.1:8000";

export async function uploadResumes(file) {
    const data = new FormData();

    data.append("file", file);

    const response = await fetch(
        `${BASE}/upload-resumes`,
        {
            method: "POST",
            body: data
        }
    );

    return await response.json();
}

export async function searchCandidates(query) {
    const response = await fetch(
        `${BASE}/search?query=${query}`
    );

    return await response.json();
}

// export async function recruiterChat(message) {
//     const response = await fetch (
//         `http://127.0.0.1:8000/chat?message=${encodeURIComponent(message)}`
//     )

//     return response.json()
// }