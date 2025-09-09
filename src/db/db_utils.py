from sqlalchemy import create_engine

def get_sqlite_engine(db_path="data/app_market.db"):
    """Создать подключение к SQLite (локальное MVP)."""
    return create_engine(f"sqlite:///{db_path}")

def get_postgres_engine(user="appuser", password="password",
                        host="localhost", port=5432, db="app_market"):
    """Создать подключение к PostgreSQL (через Docker)."""
    return create_engine(f"postgresql://{user}:{password}@{host}:{port}/{db}")
