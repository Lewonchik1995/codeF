from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import sqlite3

app = FastAPI()

# Разрешаем запросы с любых источников
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class Ad(BaseModel):
    title: str
    description: str
    price: float
    phone_number: str


# Функция для просмотра всех объявлений
@app.get("/ads")
def view_ads():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute("SELECT * FROM ads")
    ads = c.fetchall()

    conn.close()

    return {"ads": ads}


# Функция для добавления объявления
@app.post("/ads")
def add_ad(ad: Ad):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute("INSERT INTO ads (title, description, price, phone_number) VALUES (?, ?, ?, ?)",
              (ad.title, ad.description, ad.price, ad.phone_number))

    conn.commit()
    conn.close()

    return {"message": "Объявление успешно добавлено"}


# Функция для изменения цены объявления
@app.put("/ads/{ad_id}")
def update_price(ad_id: int, new_price: float):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute("UPDATE ads SET price = ? WHERE id = ?", (new_price, ad_id))

    conn.commit()
    conn.close()

    return {"message": "Цена объявления успешно изменена"}


# Функция для удаления объявления
@app.delete("/ads/{ad_id}")
def delete_ad(ad_id: int):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute("DELETE FROM ads WHERE id = ?", (ad_id,))

    conn.commit()
    conn.close()

    return {"message": "Объявление успешно удалено"}


# Функция для поиска объявления по названию
@app.get("/ads/{title}")
def find_ad(title: str):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute("SELECT * FROM ads WHERE title = ?", (title,))
    ad = c.fetchone()

    conn.close()

    if ad:
        return {"ad": ad}
    else:
        return {"message": "Объявление не найдено"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
