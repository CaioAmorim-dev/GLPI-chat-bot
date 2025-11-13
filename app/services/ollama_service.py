import requests

def analisar_descricao_chamado(description: str):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "phi3",
        "prompt": f"""
        Analise e padronize o chamado abaixo:
        "{description}"

        Retorne em JSON:
        {{
            "titulo": "",
            "categoria": "",
            "descricao": ""
        }}
        """
    }
    response = requests.post(url, json=payload)
    return response.json()
