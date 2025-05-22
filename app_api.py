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
    # Сохраняем загруженное изображение
    input_path = "test_img.jpg"
    with open(input_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Запускаем модель
    results = model(input_path, save=True, project="results", name="predict", exist_ok=True)

    # Получаем путь к изображению с результатами
    result_path = "test_img.jpg"

    # Возвращаем результат пользователю
    return FileResponse(result_path, media_type="image/jpeg")

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=5000)
