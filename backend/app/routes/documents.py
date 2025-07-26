from utils.db_utils import insert_document

@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    text = extract_text_from_file(file)
    
    # Break into chunks and store in DB
    chunks = [text[i:i+500] for i in range(0, len(text), 500)]
    for chunk in chunks:
        insert_document(file.filename, chunk)
    
    # Also process embeddings
    process_document(file.filename, text)
    
    return {"status": "Document processed, stored, and indexed"}
