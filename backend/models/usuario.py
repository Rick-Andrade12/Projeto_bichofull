from sqlalchemy import Column, String, Integer
from database import Base

class Usuario(Base):
    __tablename__ = 'usuarios'
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(100), index=True, unique=True, nullable=False)
    senha = Column( String(300), nullable=False)
    
    def __init__ (self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha
    