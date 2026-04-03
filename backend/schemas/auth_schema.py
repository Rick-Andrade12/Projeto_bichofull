from pydantic import BaseModel, ConfigDict


class LoginUsuario(BaseModel):
    email: str
    senha: str
    
    model_config = ConfigDict(from_attributes=True)


class TokenResposta(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str
    
    model_config = ConfigDict(from_attributes=True)