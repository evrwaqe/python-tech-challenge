import os
import openai
import json
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

SYSTEM_PROMPT = (
    "Você é um assistente que extrai filtros de busca de carros com base em uma mensagem do usuário.\n"
    "Retorne um JSON com os seguintes campos opcionais: brand, model, year, fuel, min_price, max_price.\n"
    "Se não encontrar um dado, apenas omita. Responda apenas com JSON válido, sem explicações."
)


def extract_filters(user_input: str) -> dict:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_input}
        ],
        temperature=0.2,
    )

    try:
        content = response.choices[0].message.content.strip()
        return json.loads(content)
    except Exception as e:
        print("[Error parsing filters]:", e)
        return {}
