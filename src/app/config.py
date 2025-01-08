import os


def get_postgres_uri():
    host = os.environ.get("POSTGRES_HOST", "localhost")
    port = 54321 if host == "localhost" else 5432
    password = os.environ.get("POSTGRES_PASSWORD", "abc123")
    user = os.environ.get("POSTGRES_USER", "abc123")
    db_name = os.environ.get("POSTGRES_DB", "abc123")
    return f"postgresql://{user}:{password}@{host}:{port}/{db_name}"