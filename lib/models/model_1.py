from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ExampleModel(Base):
    __tablename__ = 'example_model'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)

    def __repr__(self):
        return f"<ExampleModel(id={self.id}, name={self.name})>"