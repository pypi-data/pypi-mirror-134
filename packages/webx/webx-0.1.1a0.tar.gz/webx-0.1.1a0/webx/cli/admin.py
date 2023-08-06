from time import sleep

import click
import rich

from webx.core.management.boilerplate import _setup as boilerplate_setup


RICH_CONSOLE = rich.get_console()

@click.group()
def admin():
    pass

@admin.command()
@click.option("--name", help="The name of the project you wish to create.")
def createproject(name: str):
    with RICH_CONSOLE.status("[bold green]Creating new WebX project...") as status:
        boilerplate_setup.generate_boilerplate(name)
        sleep(1)

    rich.print(f"Project [bold cyan]{name}[/bold cyan] [bold green]successfully created.[/bold green]")

@admin.command()
def createapp():
    pass

if __name__ == "__main__":
    admin()