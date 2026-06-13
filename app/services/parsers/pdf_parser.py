# This function opens a PDF file using PyMuPDF (fitz), reads the text from each page, and stores it in a list. It then combines the text from all pages into a single string separated by newlines. Finally, it closes the PDF and returns the complete extracted text.

import fitz

def extract_text(
        pdf_path: str
):
    
    document = fitz.open(
        pdf_path
    )

    pages = []

    for page in document:

        text = page.get_text()

        pages.append(text)

    document.close()

    return "\n".join(
        pages
    )