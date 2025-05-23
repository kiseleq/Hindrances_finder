from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
from ultralytics import YOLO
import shutil
import os

app = FastAPI()

# Загружаем модель
model = YOLO("best.pt")

@app.get("/health")
def health():
    return {"status": "OK"}

@app.post("/predict_image")
def predict_image(file: UploadFile = File(...)):
    os.makedirs("images", exist_ok=True)

    input_path = "images/test_img.jpg"
    with open(input_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    results = model.predict(input_path, conf=0.5)

    output_path = "images/result.jpg"
    results[0].save(filename=output_path)

    return FileResponse(output_path, media_type="image/jpeg")

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=5000)