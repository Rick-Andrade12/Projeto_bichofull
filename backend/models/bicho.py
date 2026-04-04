from sqlalchemy import Column, String, Integer
from database import Base

class Bicho(Base):
    __tablename__ = "bichos"

    id = Column(Integer, primary_key=True, index=True)
    grupo = Column(Integer, unique=True, nullable=False)
    nome = Column(String(50), unique=True, nullable=False)
    
    def __init__ (self, grupo, nome):
        self.grupo = grupo
        self.nome = nome