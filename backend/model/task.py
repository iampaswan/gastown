
from sqlalchemy import Column, String
from db import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(String, primary_key=True)
    repo = Column(String)
    status = Column(String)