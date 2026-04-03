from sqlalchemy import Column, String, Integer, ForeignKey
from database import Base

class Sorteio(Base):
    __tablename__ = "sorteios"

    id = Column(Integer, primary_key=True, index=True)
    rodada = Column(Integer, nullable=False, index=True)
    posicao = Column(Integer, nullable=False)
    grupo = Column(Integer, ForeignKey("bichos.grupo"), nullable=False)
    milhar = Column(String(4), nullable=False)

    def __init__(self, rodada, posicao, grupo, milhar):
        self.rodada = rodada
        self.posicao = posicao
        self.grupo = grupo
        self.milhar = milhar