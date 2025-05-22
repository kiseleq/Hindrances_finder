import streamlit as st
import requests
from PIL import Image
from io import BytesIO

# Адрес FastAPI-сервера
API_URL = "http://127.0.0.1:5000/predict_image"

st.set_page_config(page_title="Hindrance Finder", layout="centered")
st.title("🧠 Hindrance Finder")
st.markdown("Загрузите изображение, и модель определит помехи")

# Интерфейс загрузки файла
uploaded_file = st.file_uploader("Выберите изображение", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Отображаем оригинал
    st.image(uploaded_file, caption="Загруженное изображение")

    # Кнопка запуска предсказания
    if st.button("📊 Предсказать"):
        with st.spinner("Отправка изображения на сервер..."):
            # Отправляем файл на FastAPI-сервер
            files = {"file": uploaded_file.getvalue()}
            response = requests.post(API_URL, files={"file": (uploaded_file.name, uploaded_file, uploaded_file.type)})

            if response.status_code == 200:
                # Преобразуем ответ в изображение
                image = Image.open(BytesIO(response.content))
                st.image(image, caption="Результат предсказания")
            else:
                st.error(f"Ошибка сервера: {response.status_code}")
