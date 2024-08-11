from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import create_database, database_exists

from app.core.config import settings

def get_engine():
    db_engine = create_engine(settings.db.DATABASE_URL, pool_pre_ping=True)

    if not database_exists(db_engine.url):
        create_database(db_engine.url)

    return db_engine


engine = get_engine()
SessionFactory = sessionmaker(autocommit=False, autoflush=False, expire_on_commit=False, bind=engine)


def get_db_session():
    return SessionFactory()