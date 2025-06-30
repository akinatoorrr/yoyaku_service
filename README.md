# yoyaku_service
Простой REST-сервис для управления номерами отелей и их бронированием.

## Функциональность

### Rooms (номера отеля)

- **POST /rooms/** — создать номер
- **GET /rooms/** — получить список номеров с сортировкой (по цене или дате)
- **DELETE /rooms/{id}/** — удалить номер и все его брони

### Bookings (бронирования)

- **POST /bookings/** — создать бронь на номер
- **GET /bookings/?room_id={room_id}** — получить список броней для номера
- **DELETE /bookings/{id}/** — удалить бронь

---

## 🧪 Примеры curl-запросов

### ▶ Добавление номера

```bash
curl -X POST http://localhost:8000/rooms/ \
  -d "room_number=101" \
  -d "description=Уютный номер с окном" \
  -d "price_per_night=4500"
````

📥 Ответ:

```json
{
  "id": 1,
  "room_number": 101,
  "description": "Уютный номер с окном",
  "price_per_night": 4500,
  "created_at": "2025-06-30T15:00:00Z"
}
```

### ▶ Получение списка номеров (с сортировкой)

```bash
curl -X GET "http://localhost:8000/rooms/?ordering=-price_per_night"
```

---

### ▶ Удаление номера

```bash
curl -X DELETE http://localhost:8000/rooms/1/
```

---

### ▶ Создание брони

```bash
curl -X POST http://localhost:8000/bookings/ \
  -d "room=1" \
  -d "date_start=2025-07-10" \
  -d "date_end=2025-07-12"
```

📥 Ответ:

```json
{
  "id": 44,
  "room": 1,
  "date_start": "2025-07-10T00:00:00Z",
  "date_end": "2025-07-12T00:00:00Z"
}
```

---

### ▶ Получение броней номера

```bash
curl -X GET "http://localhost:8000/bookings/?room_id=1"
```

📥 Ответ:

```json
[
  {
    "id": 44,
    "room": 1,
    "date_start": "2025-07-10T00:00:00Z",
    "date_end": "2025-07-12T00:00:00Z"
  }
]
```

---

## 🚀 Запуск проекта

### 📦 Через Docker (рекомендуется)

```bash
docker-compose up --build
```

### 🛠 Локально

1. Установите зависимости:

   ```bash
   poetry install
   ```

2. Настройте `.env` или переменные окружения для подключения к PostgreSQL. В репозитории есть пример того, какие переменные ожидаются

3. Выполните миграции из директории yoyaku/:

   ```bash
   python manage.py migrate
   ```

4. Запустите сервер:

   ```bash
   python manage.py runserver
   ```
