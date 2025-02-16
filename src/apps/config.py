import os


def get_postgres_uri():
    host = os.environ.get("POSTGRES_HOST", "localhost")
    port = int(os.environ.get("POSTGRES_PORT", 5432)) if host != "localhost" else 54321
    password = os.environ.get("POSTGRES_PASSWORD", "abc123")
    user = os.environ.get("POSTGRES_USER", "abc123")
    db_name = os.environ.get("POSTGRES_DB", "abc123")
    return f"postgresql://{user}:{password}@{host}:{port}/{db_name}"

