from fastapi import APIRouter, Request, Response
from app.services.whatsapp_service import send_message

router = APIRouter()

@router.post("/webhook/whatsapp")
async def receive_message(request: Request):
    data = await request.form()
    user_message = data.get("Body")
    user_number = data.get("From")

    print(f"📩 Mensagem recebida de {user_number}: {user_message}")

    # Resposta simples (teste inicial)
    resposta = "Olá! 👋 Sou o assistente técnico da SDS-PE.\nComo posso te ajudar hoje?"
    send_message(user_number, resposta)

    return Response(content="OK", status_code=200)
