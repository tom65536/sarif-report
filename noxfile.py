
import nox


@nox.session
def test(ctx: nox.Session) -> None:
    """Run unit tests."""
    ctx.install('pytest', 'pytest-click', '.')
    ctx.run('pytest')
