from fastapi import Depends, HTTPException
from database import SessionLocal
from sqlalchemy.orm import Session
from models.usuario import Usuario
from jose import jwt, JWTError
from security import SECRECT_KEY, ALGORITHM, oauth2_schema

def pegar_sessao():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
        
        
def verificar_token(token: str = Depends(oauth2_schema), session: Session = Depends(pegar_sessao)):
    try:
        dic_inf = jwt.decode(token, SECRECT_KEY, algorithms=[ALGORITHM])
        id_usuario = int(dic_inf.get('sub'))
    except JWTError:
        raise HTTPException(status_code=401, detail='Acesso negado')

    usuario = session.query(Usuario).filter(Usuario.id==id_usuario).first()
    if not usuario:
        raise HTTPException(status_code=401, detail='Acesso invalido')
    return usuario