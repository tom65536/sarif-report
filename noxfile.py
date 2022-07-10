"""Sessions for nox."""
import pathlib

import nox


TARGET_PATH = pathlib.Path("target")
LINT_REPORT_PATH = TARGET_PATH / "lint"


@nox.session
def test(ctx: nox.Session) -> None:
    """Run unit tests."""
    ctx.install("pytest", "pytest-click", ".")
    ctx.run("pytest")


@nox.session
def lint(ctx: nox.Session) -> None:
    """Run static code analysis."""
    LINT_REPORT_PATH.mkdir(exist_ok=True, parents=True)
    ctx.install(
        "pylama[all]",
    )

    args = [
        "--report",
        f'{LINT_REPORT_PATH/"lint-report.json"}',
    ]
    if ctx.posargs:
        args += ctx.posargs

    ctx.run("pylama", *args)
