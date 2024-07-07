from __future__ import annotations
from typing import TYPE_CHECKING

import rich_click as click


@click.group()
def cli():
    pass    
    
@cli.command()
@cli.option("--scope", "-s", type=click.STRING, help="the path of a .txt file where the scope is stored. each row is a host/artifact/tag", required=True) 
def run(scope: str):
    click.echo(f"Scope: {scope}")
    
    with open(scope) as f:
        for line in f:
            click.echo(f"Line: {line}")
            
    click.echo("Done.")
    
    
    


        