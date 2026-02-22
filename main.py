from fastapi import FastAPI, UploadFile, File
import cv2
import shutil
import os

app = FastAPI()

@app.post("/process")
async def process_image(file: UploadFile = File(...)):
    input_path = f"temp_{file.filename}"

    with open(input_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    img = cv2.imread(input_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    output_path = f"processed_{file.filename}"
    cv2.imwrite(output_path, gray)

    return {"message": "processed", "file": output_path}