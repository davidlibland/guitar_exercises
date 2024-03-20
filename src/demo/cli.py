"""
This script exports a randomly generated file.
"""
import random
import sys
from importlib import resources

import click
import pandas

modes


@click.cli
def cli():
    pass

@cli.command()
def random_scale():
    scale = random.choice(["I (Ionian)", "ii (Dorian)"])

@click.command()
@click.argument("nsubjects", type=int)
@click.option("--output", "-o", type=click.File(mode="w"), default="-")
def export_dm(nsubjects: int, output: click.File) -> int:
    """
    Export a csv file of randomly-generated demographics data.

    Args:
        nsubjects: number of subjects to generate in the table
        output: which file to write the output to

    Returns:
        exit_code - 0 if successful, or negative if error
    """
    if nsubjects < 1:
        click.secho(
            "Must generate at least one subject.",
            bold=True,
            fg="red",
            err=True,
        )
        return sys.exit(-1)

    table = random_demographics_table(nsubjects)
    df = pandas.DataFrame(data=table.data)
    click.secho(">> Generated table: ", bold=True, fg="green", err=True)
    click.secho(df.tail().to_string(), err=True)

    output_name = getattr(output, "name", "stdout")
    click.secho(
        f">> Rendering table to {output_name}", bold=True, fg="green", err=True
    )
    df.to_csv(output)

    return sys.exit(0)


@click.command()
def print_sample():
    """
    Print the "data/sample.csv" file.

    Returns:
        exit_code: 0 for success
    """

    # load data from packaged resources file
    with resources.path("demo.data", "sample.csv") as path:
        df = pandas.read_csv(path)

    click.secho(">> Sample table: ", bold=True, fg="green", err=True)
    click.secho(df.tail().to_string(), err=True)

    return sys.exit(0)
