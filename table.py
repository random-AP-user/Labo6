from rich.console import Console
from rich.table import Table


def table(content):
    table = Table(title="Star Wars Movies")
    for fields in content[0]:
        table.add_column(f"{fields}", justify="right", style="cyan", no_wrap=True)
    console = Console()
    for fields in content[1:]:
        table.add_row(fields[0], fields[1],fields[2])
    console.print(table)

def main():
    table([[]])


if __name__ == "__main__":
    main()