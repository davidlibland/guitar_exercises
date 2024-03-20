"""
This script exports a randomly generated file.
"""
import random
import sys
from importlib import resources

import click
import pandas

modes = [
    "I (Ionian)",
    "ii (Dorian)",
    "iii (Phyrigian)",
    "IV (Lydian)",
    "V (Mixolydian)",
    "vi (Aolian)",
    "viiDim (Locrian)"
]
notes = [
    "A",
    "A#/Bb"
    "C",
    "C#/Db",
    "D",
    "D#/Eb",
    "E",
    "F",
    "F#/Gb",
    "G",
    "G#/Ab"
]


@click.group()
def cli():
    pass

@cli.command()
def random_scale():
    scale = random.choice(modes)
    root = random.choice(notes)
    position = random.choice(list("CAGED"))
    click.echo(f"Play {root} {scale} in the {position} position.")


if __name__ == "__main__":
    cli()