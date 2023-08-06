import click
from rich.table import Table
from rich import print as rich_print

from webx.httpclient.backends.sync import SyncHTTPClientBackend


@click.group()
def monitor():
    pass

@monitor.command()
@click.option("--site", help="Where to fetch.", default="http://localhost:8000")
@click.option("--path", help="The monitor path", default="/webx-monitor")
@click.option("--auth", help="Authorization")
def stats(site: str, path: str, auth: str):
    backend = SyncHTTPClientBackend()
    url = site + path

    headers = {
        "Authorization": auth
    }
    try:
        response = backend.request("GET", url, headers=headers)
    except Exception as exc:
        return rich_print(f"Unable to monitor [bold cyan]{url}[/bold cyan]: [bold red]{exc}[/bold red]")

    data = response.json()
    table = Table(show_header=True, header_style="bold cyan")
    table.add_column("Stat")
    table.add_column("Value")

    for key, value in data.items():
        table.add_row(str(key), str(value))

    rich_print(table)

if __name__ == "__main__":
    monitor()