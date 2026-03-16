from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.student import router as student_router
from app.routes.professor import router as professor_router
from app.routes.chat import router as chat_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "API funcionando 🚀"}

app.include_router(student_router)
app.include_router(professor_router)
app.include_router(chat_router)