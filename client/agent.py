from client.mcp_client import send_filters
from client.nlp_interpreter import extract_filters
from prompt_toolkit import prompt
from rich import print


def run_agent():
    print("[bold cyan]Welcome to Car Finder! Describe the car you're looking for.[/bold cyan]")

    filters = {}
    while not filters:
        user_input = prompt("You: ")
        filters = extract_filters(user_input)

        if not filters:
            print(
                "[yellow]Sorry, I couldn't understand. Could you describe differently?[/yellow]")

    print("[green]Searching based on your description...[/green]")
    results = send_filters(filters)

    if not results:
        print("[red]No vehicles found with the given filters.[/red]")
    else:
        print(f"[green]{len(results)} vehicles found:[/green]")
        for v in results:
            print(
                f"- [bold]{v['brand']} {v['model']}[/bold], {v['year']} - {v['color']} - {v['mileage']} km - R${v['price']:.2f}")


if __name__ == "__main__":
    run_agent()
