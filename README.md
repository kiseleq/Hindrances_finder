
# Hindrances Finder

Этот проект для автоматического поиска препятствий (hindrance) на изображениях с использованием компьютерного зрения.

---

## Содержание

- [Пример работы детектора](#Пример-работы-детектора)
- [Установка](#установка)
- [Запуск](#запуск)
  - [FastAPI (Backend)](#fastapi-backend)
  - [Streamlit (Frontend)](#streamlit-frontend)
- [Формат запроса](#формат-запроса)
- [Конфигурация](#конфигурация)
- [Обратная связь](#обратная-связь)

---

## Пример работы детектора



| Исходное изображение        | Обработанное изображение     |
|-----------------------------|------------------------------|
| ![Исходное](images/test_img.jpg) | ![Обработанное](images/result.jpg) |

| Исходное изображение        | Обработанное изображение     |
|-----------------------------|------------------------------|
| ![Исходное](images/test_img2.jpg) | ![Обработанное](images/result2.jpg) |

---

## Установка

1. Клонируйте репозиторий:
```bash
git clone -b i.fronin https://github.com/kiseleq/Hindrances_finder.git
cd Hindrances_finder
```

2. Установите зависимости:

```bash
pip install -r requirements.txt
```

3. Загрузите веса модели в папку models/

---

## Запуск

### FastAPI (Backend)

Запуск сервера:
```bash
uvicorn app_api:app --reload --host 127.0.0.1 --port 5000
```

Сервер будет доступен по адресу: http://127.0.0.1:5000

Пример запроса:
```bash
curl -X POST http://127.0.0.1:5000/detect \
     -F "file=@test_image.jpg" \
     -H "Content-Type: multipart/form-data"
```

### Streamlit (Frontend)

Запуск веб-приложения:
```bash
streamlit run srteamlit_app.py --server.port 5000
```

Веб-интерфейс подключается к API по адресу `http://localhost:5000`.

---

## Обратная связь

Если вы нашли ошибку или у вас есть предложения по улучшению, создайте issue или pull request!
Вы также можете связаться с командой напрямую: **xxxxx@yandex.ru**