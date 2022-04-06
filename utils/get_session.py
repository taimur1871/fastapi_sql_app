from sqlalchemy.orm import Session


def create_session(engine):
    """
    Creates a session for the database.
    """
    session = Session(engine)
    return session
