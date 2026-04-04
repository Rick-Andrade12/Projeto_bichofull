from pydantic import BaseModel, ConfigDict


class CarteiraResposta(BaseModel):
    id: int
    usuario_id: int
    saldo: float

    model_config = ConfigDict(from_attributes=True)