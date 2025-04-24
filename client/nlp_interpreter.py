import os
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("GROQ_API_KEY"),
                base_url="https://api.groq.com/openai/v1")

SYSTEM_PROMPT = (
    "You are an assistant that extracts car search filters based on a user's phrase.\n"
    "Only return a JSON with the following fields if you can extract it: brand, model, year, fuel, min_price, max_price.\n"
    "Don't explain anything. Example of correct answer:\n"
    "{\"brand\": \"Honda\", \"model\": \"hatchback\", \"fuel\": \"Gasoline\", \"year\": 2019}"
)


def extract_filters(user_input: str) -> dict:
    try:
        response = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_input}
            ],
            temperature=0.2
        )
        content = response.choices[0].message.content.strip()
        print("[Groq response]:", content)
        return json.loads(content)
    except Exception as e:
        print("[Error parsing filters]:", e)
        return {}
