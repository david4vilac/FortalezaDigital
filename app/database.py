from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
 
SQLALCHEMY_DATABASE_URL = "postgresql://szfbkmrh:8tO_Ea4IU9O8GdS47w8rxP1BUyWU8KKQ@queenie.db.elephantsql.com:5432/szfbkmrh"
 
engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
 
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
 
Base = declarative_base()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()