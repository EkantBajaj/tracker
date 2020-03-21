from sqlalchemy import create_engine
from sqlalchemy.engine.url import  URL
from sqlalchemy.orm import scoped_session,sessionmaker
from sqlalchemy_mptt import mptt_sessionmaker

db_session = scoped_session(mptt_sessionmaker(sessionmaker(
    autocommit=False, autoflush=False)))