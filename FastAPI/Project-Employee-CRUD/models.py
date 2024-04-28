from sqlalchemy import Column, Integer, String

from database import Base

class Employee(Base) :
    __tablename__ = "employee"

    id = Column(Integer, primary_key=True, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=True)
    email = Column(String, nullable=False)