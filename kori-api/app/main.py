from fastapi import FastAPI
from app.database import get_connection

app = FastAPI()


@app.get("/")
def root():
    return {"message": "API funcionando 🚀"}


@app.get("/test-db")
def test_db():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT 1;")
    result = cur.fetchone()

    conn.close()

    return {"database": result}