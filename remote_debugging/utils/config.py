from os import environ


def _create_sql_alchemy_url(
    db_url: str, db_user: str, db_pass: str, db_name: str
) -> str:
    return "postgresql+psycopg2://%(user)s:%(pass)s@%(url)s/%(name)s" % {
        "user": db_user,
        "pass": db_pass,
        "name": db_name,
        "url": db_url,
    }


class Config:
    """
    Common configurations
    """

    db_url = environ.get("DB_URL")
    db_user = environ.get("DB_USER")
    db_pass = environ.get("DB_PASS")
    db_name = environ.get("DB_NAME")

    SQLALCHEMY_DATABASE_URI = _create_sql_alchemy_url(db_url, db_user, db_pass, db_name)
