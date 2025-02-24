import sqlite3
import json

DB_FILE = "films.db"
OUTPUT_JSON = "films.json"

def export_to_json():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor() #объект соединения с бд

    cursor.execute("SELECT id, title, release_year, director, producers, box_office, country FROM films")
    films = cursor.fetchall() # создаёт объект курсора (cursor), который позволяет выполнять SQL-запросы к базе данных

    films_list = []
    for film in films:
        films_list.append({
            "id": film[0],
            "title": film[1],
            "year": film[2],
            "director": film[3],
            "producers": film[4],
            "box_office": film[5],
            "country": film[6]
        })

    #dump:Используется для записи объектов (сериализованных объектов Python) в файл в формате JSON
    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(films_list, f, indent=4)

    conn.close()
    print(f"DATA SAVED IN {OUTPUT_JSON}")

export_to_json()
