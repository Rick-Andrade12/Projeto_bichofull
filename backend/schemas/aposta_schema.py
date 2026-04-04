from pydantic import BaseModel, ConfigDict
from typing import Optional


class ApostaCreate(BaseModel):
    tipo: str
    numero: str
    valor: float

    model_config = ConfigDict(from_attributes=True)


class ApostaResposta(BaseModel):
    id: int
    usuario_id: int
    tipo: str
    numero: str
    valor: float
    premio: float
    status: str
    posicao_premiada: Optional[int] = None

    model_config = ConfigDict(from_attributes=True)