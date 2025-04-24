from client.nlp_interpreter import extract_filters
from client.mcp_client import send_filters
from rich import print
from rich.panel import Panel


def run_agent():
    print(Panel("Welcome to Car Finder!", style="bold cyan"))

    while True:
        print(
            "\n[bold yellow]Describe the car you're looking for (or type 'exit' to quit):[/bold yellow]")
        user_input = input("You: ")

        if user_input.strip().lower() in ("exit", "sair", "quit"):
            print("[bold cyan]Goodbye![/bold cyan]")
            break

        filters = extract_filters(user_input)

        if not filters:
            print(
                "[red]I couldn't understand that. Try describing it differently.[/red]")
            continue

        print("[blue]Searching based on your description...[/blue]")
        vehicles = send_filters(filters)

        if not vehicles:
            print("[bold red]No vehicles found. Try adjusting your search.[/bold red]")
        else:
            print(
                f"[bold green]Found {len(vehicles)} vehicle(s):[/bold green]\n")
            for v in vehicles:
                print(
                    f"[green]- {v['brand']} {v['model']} ({v['year']})[/green] "
                    f"[white]— {v['color']}, {v['mileage']}km, R$ {v['price']:.2f}[/white]"
                )
