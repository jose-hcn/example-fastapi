from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from .config import settings

SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)

class Base(DeclarativeBase):
    pass

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


#while True:
#    try:
#        conn = psycopg2.connect(host = 'localhost', database = 'fastapi', user = 'postgres',
#                                password = 'upfeupJn?2', cursor_factory = RealDictCursor)
#
#        cursor = conn.cursor()
#        print('Database connection was successful!')
#        break
#    except Exception as error:
#        print("Connecting to database failed")
#        print("Error: ", error)
#        time.sleep(2)
