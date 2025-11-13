import requests
from app.config import settings

def enviar_mensagem(phone: str, message: str):
    url = f"{settings.WPP_BASE_URL}/api/{settings.WPP_SESSION}/send-message"
    payload = {"phone": phone, "message": message}
    headers = {"Authorization": settings.WPP_TOKEN}
    response = requests.post(url, json=payload, headers=headers)
    return response.json()
