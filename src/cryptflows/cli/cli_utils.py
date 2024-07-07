from __future__ import annotations
from typing import TYPE_CHECKING

import rich_click as click

from ..workflows.tasking.scope_management import parse_scope_input_file_into_list_of_strings



def run_analysis(scope: str):
    
    click.echo(f"[green]Running analysis on scope: {scope}[/green]")
    
    scope_asset_lists = parse_scope_input_file_into_list_of_strings(scope_filepath=scope)

    click.echo(f"[green]Running analysis on assets provided in scope: {scope_asset_lists}[/green]")
    
    click.echo("Done.")
    
    
    


        