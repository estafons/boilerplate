import nox


@nox.session(python="3.10")
def tests(session):
    session.install("-r", "requirements.txt")
    session.install("pytest")
    session.run("pytest")
