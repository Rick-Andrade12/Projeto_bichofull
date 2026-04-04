from pydantic import BaseModel, ConfigDict


class SorteioCreate(BaseModel):
    rodada: int
    posicao: int
    grupo: int
    milhar: str

    model_config = ConfigDict(from_attributes=True)


class SorteioResposta(BaseModel):
    id: int
    rodada: int
    posicao: int
    grupo: int
    milhar: str

    model_config = ConfigDict(from_attributes=True)