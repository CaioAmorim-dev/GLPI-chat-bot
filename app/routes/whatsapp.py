from fastapi import APIRouter, Request
import json

router = APIRouter()

@router.post("/webhook/wpp")
async def wpp_webhook(request: Request):
    body = await request.body()
    
    try:
        data = json.loads(body)
    except:
        return {"status": "invalid_json"}

    # Exibe todo o conteúdo recebido do WPPConnect
    print("📩 Mensagem recebida do WPPConnect:", data)

    # Quando uma mensagem chega no WhatsApp
    if "messages" in data and len(data["messages"]) > 0:
        msg = data["messages"][0]
        sender = msg["from"]
        text = msg["body"]

        print(f"💬 Mensagem de {sender}: {text}")

    return {"status": "ok"}
