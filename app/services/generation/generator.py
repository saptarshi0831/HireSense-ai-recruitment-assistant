def summarize_resume(text: str):
    lines = (
        text
        .replace("\n\n", "\n")
        .split("\n")
    )


    new_lines = []

    for x in lines:
        if x.strip():
            new_lines.append(x.strip())

    lines = new_lines

    summary = "\n".join(
        lines[:15]
    )

    return summary