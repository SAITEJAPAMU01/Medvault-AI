import os
from fastapi import FastAPI, UploadFile, File, HTTPException
from dotenv import load_dotenv
from . import security

# Load environment variables
load_dotenv()

app = FastAPI(title="MedVault AI")

@app.get("/")
def home():
    return {"status": "Online", "message": "MedVault AI Server is running!"}

@app.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    try:
        # Read the file
        content = await file.read()
        text_content = content.decode("utf-8")

        # Encrypt it
        encrypted_data = security.encrypt_medical_data(text_content)

        # Save to the data folder
        file_path = os.path.join("backend/data", f"{file.filename}.enc")
        with open(file_path, "w") as f:
            f.write(encrypted_data)

        return {"filename": file.filename, "message": "Encrypted successfully!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/ask")
def ask_ai(query: str):
    # This is our placeholder for Gemini and Pinecone next
    return {"query": query, "response": "Backend logic ready. Next step: Connect Gemini API."}