"""Test cases for the main program."""
import sarif_report.__main__ as main


def test_main(cli_runner) -> None:
    """Run the main program."""
    result = cli_runner.invoke(main.hello, [])
    assert result.exit_code == 0
    assert result.output.strip() == "Hello there"
