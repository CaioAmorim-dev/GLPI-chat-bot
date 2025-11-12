from fastapi import FastAPI
from app.config import settings

app = FastAPI()

@app.get("/")
def root():
    return {"msg": "Bot SDS-PE rodando com sucesso!", "GLPI_URL": settings.GLPI_URL}
