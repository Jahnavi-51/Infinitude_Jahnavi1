from sqlalchemy import Column, Integer, String
from Database import Base

class Course(Base):
    __tablename__ = "courses"

    Id = Column(Integer,primary_key=True)
    Name = Column(String)
    Price = Column(Integer)