from fastapi import FastAPI
from app.config import settings
from app.routes import whatsapp 

app = FastAPI()

@app.get("/")
def root():
    return {"msg": "Bot SDS-PE rodando com sucesso!", "GLPI_URL": settings.GLPI_URL}

# Adiciona o router de WhatsApp
app.include_router(whatsapp.router)