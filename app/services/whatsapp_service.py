import requests
from app.config import settings


def send_message(to: str, message: str):
    """
    Envia uma mensagem WhatsApp usando a API do Twilio.

    Parâmetros:
        to (str): Número do destinatário (com ou sem 'whatsapp:')
        message (str): Corpo da mensagem a ser enviada

    Retorna:
        dict: Resposta JSON da API do Twilio
    """

    # Garante que o número esteja no formato exigido
    if not to.startswith("whatsapp:"):
        to = f"whatsapp:{to}"

    url = f"https://api.twilio.com/2010-04-01/Accounts/{settings.TWILIO_ACCOUNT_SID}/Messages.json"

    payload = {
        "From": f"whatsapp:{settings.TWILIO_WHATSAPP_NUMBER}",
        "To": to,
        "Body": message
    }

    # Requisição autenticada via HTTP Basic Auth
    response = requests.post(
        url,
        data=payload,
        auth=(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    )
