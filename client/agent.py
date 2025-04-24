from client.mcp_client import send_filters
from prompt_toolkit import prompt
from rich import print


def ask_user() -> dict:
    print("[bold cyan]Welcome to Car Finder![/bold cyan]")
    filters = {}

    brand = prompt("Do you have a brand in mind? (press Enter to skip): ")
    if brand:
        filters["brand"] = brand

    fuel = prompt("Preferred fuel type? (e.g. Gasoline, Diesel, Electric): ")
    if fuel:
        filters["fuel"] = fuel

    year = prompt("From which year onwards? (e.g. 2015): ")
    if year.isdigit():
        filters["year"] = int(year)

    return filters


def show_results(results: list):
    if not results:
        print("[red]No vehicles found with the given filters.[/red]")
    else:
        print(f"[green]{len(results)} vehicles found:[/green]")
        for v in results:
            print(
                f"- [bold]{v['brand']} {v['model']}[/bold], {v['year']} - {v['color']} - {v['mileage']} km - R${v['price']:.2f}")


def run_agent():
    filters = ask_user()
    results = send_filters(filters)
    show_results(results)


if __name__ == "__main__":
    run_agent()
