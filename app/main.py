from fastapi import FastAPI, Request
from app.services.wppconnect_service import send_message

app = FastAPI()

@app.get("/")
def root():
    return {"status": "Bot SDS-PE rodando!"}