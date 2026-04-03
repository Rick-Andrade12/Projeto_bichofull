from sqlalchemy import Column, String, Integer, Float, ForeignKey
from database import Base

class Aposta(Base):
    __tablename__ = 'apostas'
    
    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'), nullable=False)
    tipo = Column(String(100), nullable=False)
    numero = Column(String(4), nullable=False)
    valor = Column(Float, nullable=False)
    status = Column(String(100), nullable=False, default='pendente')
    premio = Column(Float, nullable=False, default=0.0)
    posicao_premiada = Column(Integer, nullable=True)

    def __init__(self, usuario_id, tipo, numero, valor, status='pendente', premio=0.0, posicao_premiada=None):
        self.usuario_id = usuario_id
        self.tipo = tipo
        self.numero = numero
        self.valor = valor
        self.status = status
        self.premio = premio
        self.posicao_premiada = posicao_premiada