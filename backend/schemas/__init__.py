# from pydantic import BaseModel, ConfigDict, EmailStr

# class UsuarioCreate(BaseModel):
#     nome: str
#     email: EmailStr
#     senha: str
    
#     model_config = ConfigDict(from_attributes = True)
        
# class LoginUsuario(BaseModel):
#     email: EmailStr
#     senha: str
    
#     model_config = ConfigDict(from_attributes = True)
    
# class TokenResposta(BaseModel):
#     access_token: str
#     refresh_token: str
#     token_type: str
    
    
# class ApostaCreate(BaseModel):
#     tipo: str
#     numero: int
#     valor: float
    
# class ApostaResposta(BaseModel):
#     id: int
#     usuario_id: int
#     tipo: str
#     numero: str
#     valor: float
#     status: str
#     premio: float

#     model_config = ConfigDict(from_attributes=True)
    

# class SorteioResposta(BaseModel):
#     id: int
#     grupo: int
#     milhar: str

#     model_config = ConfigDict(from_attributes = True)
    

# class CarteiraResposta(BaseModel):
#     id: int
#     saldo: float
#     usuario_id: int

#     model_config = ConfigDict(from_attributes = True)
    

# class UsuarioResposta(BaseModel):
#     id: int
#     nome: str
#     email: EmailStr

#     model_config = ConfigDict(from_attributes=True)
