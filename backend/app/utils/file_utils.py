import fitz  # PyMuPDF
from docx import Document

def extract_text_from_file(file):
    if file.filename.endswith(".pdf"):
        doc = fitz.open(stream=file.file.read(), filetype="pdf")
        text = ""
        for page in doc:
            text += page.get_text()
        return text

    elif file.filename.endswith(".docx"):
        doc = Document(file.file)
        return "\n".join([p.text for p in doc.paragraphs])

    else:
        return file.file.read().decode("utf-8")
