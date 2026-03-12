# AI note: ChatGPT 5.4 Thinking was used to help debug and fix syntax. 

from rich.console import Console
from rich.table import Table
import csv
import os

console = Console()

def show_example_data():
    console.print("Here is some initial data:", style="bold cyan")
    table = Table(title="Purchases This Month")
    table.add_column("Item", style="magenta")
    table.add_column("Price", justify="right", style="green")
    table.add_row("CHOBANI YGRT", "8.645")
    table.add_row("BKD POT SOUP", "9.99")
    table.add_row("BLACKBERRIES", "4.79")
    table.add_row("MADELEINES", "9.69")
    table.add_row("DRD CHERRIES", "9.99")
    table.add_row("ORG APLSAUCE", "14.99")
    table.add_row("CHOC CHUNK", "9.99")
    table.add_row("MATCHA TRFLS", "16.99")
    table.add_row("MOZZARELLA", "7.79")
    table.add_row("ARTISAN ROLL", "5.99")
    console.print(table)

def get_purchase_entry():
    console.print("\nEnter a new purchase:", style="bold yellow")

    item = input("Enter the item name: ")
    price = input("Enter the price: ")

    return {
        "item": item,
        "price": price
    }


def show_user_entries(entries):
    table = Table(title="Your Entered Purchases")
    table.add_column("Item", style="magenta")
    table.add_column("Price", justify="right", style="green")

    for entry in entries:
        table.add_row(entry["item"], entry["price"])

    console.print(table)


def save_to_csv(entries, filename):
    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["item", "price"])
        writer.writeheader()
        writer.writerows(entries)


def main():
    show_example_data()

    confirmed_entries = []

    while True:
        entry = get_purchase_entry()

        console.print("\nYou entered:", style="bold green")
        preview = Table(title="Confirm Purchase")
        preview.add_column("Item", style="magenta")
        preview.add_column("Price", justify="right", style="green")
        preview.add_row(entry["item"], entry["price"])
        console.print(preview)

        confirm = input("Is this data correct? (yes/no): ").strip().lower()

        if confirm == "yes":
            confirmed_entries.append(entry)
            console.print("Entry confirmed.", style="bold green")
        else:
            console.print("Please re-enter the purchase.", style="bold red")
            continue

        another = input("Would you like to enter another purchase? (yes/no): ").strip().lower()
        if another != "yes":
            break

    if len(confirmed_entries) == 0:
        console.print("No data to save.", style="bold red")
        return

    show_user_entries(confirmed_entries)

    filename = input("Enter the file name (without .csv): ").strip()
    full_filename = filename + ".csv"
    save_to_csv(confirmed_entries, full_filename)

    full_path = os.path.abspath(full_filename)
    console.print(f"\nData has been saved to: {full_path}", style="bold cyan")

main()