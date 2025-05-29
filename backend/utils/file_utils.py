import os 
from uuid import uuid4
from fastapi import UploadFile

UNPLAD_DIR = "uploads"

def save_image(file: UploadFile) -> str:
    if not os.path.exists(UNPLAD_DIR):
        os.makedirs(UNPLAD_DIR)
    
    ext = file.filename.split(".")[-1]
    filename = f"{uuid4()}.{ext}"
    filepath = os.path.join(UNPLAD_DIR, filename)
    
    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())
    return file_path