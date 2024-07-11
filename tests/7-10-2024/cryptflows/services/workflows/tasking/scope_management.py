from rich_click import click



def parse_scope_input_file_into_list_of_strings(scope_filepath: str) -> str:
    
    scope_asset_lists: list = []
    
    with open(scope_filepath) as f:
        for line in f:
            click.echo(f"Host or artifact: {line}")
            scope_asset_lists.append(line)

    click.echo("Done.")
    return scope_asset_lists