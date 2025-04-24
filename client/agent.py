from client.mcp_client import send_filters
from client.nlp_interpreter import extract_filters
from openai import OpenAI
from dotenv import load_dotenv
from rich import print
from rich.panel import Panel

import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)


def run_agent():
    print(Panel("Welcome to Car Finder!", style="bold cyan"))
    print("[bold yellow]Tell me what kind of car you're looking for! You can talk about brand, fuel type, year, price range, or anything else.[/bold yellow]")

    messages = [
        {
            "role": "system",
            "content": (
                "You are a friendly and informal car assistant. Help the user find vehicles by chatting naturally. "
                "Ask questions like: 'what's the car for?', 'any preferred brand?', 'do you have a budget in mind?'. "
                "Whenever possible, say you're looking for cars based on their preferences and guide them to refine the search."
            )
        }
    ]

    while True:
        user_input = input("You: ")
        if user_input.strip().lower() in ("exit", "quit"):
            print("[bold cyan]See you next time![/bold cyan]")
            break

        messages.append({"role": "user", "content": user_input})

        try:
            response = client.chat.completions.create(
                model="llama3-70b-8192",
                messages=messages,
                temperature=0.7
            )
            reply = response.choices[0].message.content.strip()
            print(f"[bold green]Agent:[/bold green] {reply}")
            messages.append({"role": "assistant", "content": reply})

            filters = extract_filters(reply)

            if filters:
                print("[blue]Alright, let me check some options for you...[/blue]")
                vehicles = send_filters(filters)

                if not vehicles:
                    print(
                        "[red]Hmm, I couldn't find anything. Want to try a different brand or range?[/red]")
                else:
                    print(
                        f"[green]I found {len(vehicles)} car(s) that match:[/green]\n")
                    for v in vehicles:
                        print(
                            f"[white]- {v['brand']} {v['model']} ({v['year']}) — {v['color']}, {v['mileage']}km, R$ {v['price']:.2f}[/white]"
                        )
        except Exception as e:
            print("[red]Error while generating response:[/red]", e)
