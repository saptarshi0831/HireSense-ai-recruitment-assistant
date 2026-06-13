const BASE = "http://127.0.0.1:8000"

export async function uploadResume(file){
    const data = new FormData()

    data.append("file", file)

    const response = 
                    await fetch(
                        `${BASE}/upload-resume`, {
                            method: "POST",
                            body: data
                        }
                    )
        return (
            response.json()
        )
}

export async function searchCandidates(query) {
    const response = await fetch(`http://127.0.0.1:8000/search?query=${query}`)

    return response.json()
}