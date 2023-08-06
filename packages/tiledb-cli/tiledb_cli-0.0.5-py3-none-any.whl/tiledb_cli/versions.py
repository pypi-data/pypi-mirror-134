import tiledb
import click


@click.group()
def versions():
    """
    Output the TileDB version information for the Python package and
    embedded library.
    """
    pass


@click.command("tiledbpy")
def tiledbpy():
    """
    Show the TileDB-Py version
    """
    click.echo(f"TileDB-Py {tiledb.version.version}")


@click.command("tiledb")
def tiledb():
    """
    Show the TileDB Embedded (aka "libtiledb") version
    """
    click.echo(f"TileDB {'.'.join(map(str, tiledb.libtiledb.version()))}")


versions.add_command(tiledbpy)
versions.add_command(tiledb)
