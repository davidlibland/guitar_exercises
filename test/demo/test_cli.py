"""
Use the click testrunner to ensure that we can run the CLI and generate some coverage.
"""
import click.testing as c_test

from demo.cli import export_dm, print_sample


def test_print_sample():
    """ensure that we can print something using the cli"""
    runner = c_test.CliRunner()
    result = runner.invoke(
        print_sample,
        [],
        catch_exceptions=False,
    )

    assert result.exit_code == 0, "failed to run"


def test_export_dm():
    """ensure that we can generate a random demographics table"""
    runner = c_test.CliRunner()
    result = runner.invoke(
        export_dm,
        args=["10"],
        catch_exceptions=False,
    )

    assert result.exit_code == 0, "failed to run"
