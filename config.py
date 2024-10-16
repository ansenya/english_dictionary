import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import logging
logger = logging.getLogger('uvicorn.warning')

default_url = "sqlite:///./english_dictionary.db"
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", default_url)

if SQLALCHEMY_DATABASE_URL == default_url:
    logger.warning("DATABASE_URL was not set! using default - sqlite")


engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
