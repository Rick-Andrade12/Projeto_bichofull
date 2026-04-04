from sqlalchemy import Column, Integer, Float, ForeignKey
from database import Base

class Carteira(Base):
    __tablename__ = 'carteiras'
    
    id = Column(Integer, primary_key=True, index=True)
    saldo = Column(Float, default=1000.0, nullable=False)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), unique=True, nullable=False)
    
    def __init__ (self, usuario_id, saldo=1000.0):
        self.usuario_id = usuario_id
        self.saldo = saldo