from sqlalchemy import *
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Article(Base):

    __tablename__ = "articles"

    id = Column(Integer, primary_key=True)

    title = Column(String)

    url = Column(String, unique=True)

    source = Column(String)

    summary = Column(Text)

    score = Column(Float)

    published = Column(String)

class Digest(Base):

    __tablename__ = "digests"

    id = Column(Integer, primary_key=True)

    content = Column(Text)

    created_at = Column(DateTime)