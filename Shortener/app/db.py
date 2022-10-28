import os

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.exc import DBAPIError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker


# DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///foo.db")
engine = create_engine("postgresql+psycopg2://postgres:d123456@localhost:5432/shortener")
if not database_exists(engine.url):
    create_database(engine.url)

print(database_exists(engine.url))

# engine = create_engine(URL(**DATABASE))
Base = declarative_base()
DBSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db_session():
    session = DBSession()
    try:
        yield session
    except DBAPIError:
        session.rollback()
    finally:
        session.close()


class ShortenedUrl(Base):
    __tablename__ = "shortened_urls"

    id = Column(Integer, primary_key=True)
    original_url = Column(String(255))
    short_link = Column(String(255), unique=True, index=True)