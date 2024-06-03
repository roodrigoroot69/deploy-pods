from fastapi import FastAPI

app = FastAPI()

import psycopg2
from psycopg2 import sql

def connection_to_db():
    try:
        connection = psycopg2.connect(
            user="kubernetes",
            password="kubernetes123",
            host="postgresql.default.svc.cluster.local",
            port="5432",
            database="rappi"
        )
        cursor = connection.cursor()
        cursor.execute("SELECT version();")
        record = cursor.fetchone()
        print("You are connected to - ", record, "\n")

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


@app.get("/")
def read_root():
    connection_to_db()
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
