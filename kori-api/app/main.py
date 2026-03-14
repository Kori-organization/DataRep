from fastapi import FastAPI

from app.routes.student import router as student_router
from app.routes.professor import router as professor_router
from app.routes.chat import router as chat_router

app = FastAPI()


@app.get("/")
def root():
    return {"message": "API funcionando 🚀"}


app.include_router(student_router)
app.include_router(professor_router)
app.include_router(chat_router)