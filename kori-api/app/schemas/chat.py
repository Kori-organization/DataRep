from fastapi import APIRouter

router = APIRouter()

@router.get("/chat")
def chat_test():
    return {"message": "chat funcionando 🚀"}