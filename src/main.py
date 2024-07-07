from __future__ import annotations
import rich_click as click
from cryptflows.app import create_workflows_app, initialize_application_services
from datetime import datetime
#from litestar import Litestar

@click.group()
def cli():
    pass


@cli.command()
@click.argument("--scope", "-s",type=click.Path(exists=True), default="example_scope")
def run(scope: str):
    
    start_time = datetime.now()
    
    initialize_application_services()
    create_workflows_app(scope)

    click.echo(f"[green][bold]All tasks in all projects have been completed.[/bold][/green]\n\n\n[green]Started at: {start_time}\n[/green][green]Finished at: {datetime.now()}[/green]")


def main():
    cli()

if __name__ == "__main__":
    main()