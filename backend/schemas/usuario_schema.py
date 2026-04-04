from pydantic import BaseModel, EmailStr, ConfigDict


class UsuarioCreate(BaseModel):
    nome: str
    email: EmailStr
    senha: str
    
    model_config = ConfigDict(from_attributes=True)


class UsuarioResposta(BaseModel):
    id: int
    nome: str
    email: EmailStr

    model_config = ConfigDict(from_attributes=True)