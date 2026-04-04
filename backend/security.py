from passlib.context import CryptContext
from dotenv import load_dotenv
import os
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone
from models.usuario import Usuario
load_dotenv()

SECRECT_KEY = os.getenv('SECRECT_KEY')

ALGORITHM = os.getenv('ALGORITHM')

ACCESS_TOKEN_EXPIRE = int(os.getenv('ACCESS_TOKEN_EXPIRE'))

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

oauth2_schema = OAuth2PasswordBearer(tokenUrl='auth/login-form')


def criar_token(id_usuario, duracao_token=timedelta(minutes=ACCESS_TOKEN_EXPIRE)):
    data_expiracao = datetime.now(timezone.utc) + duracao_token
    dic_inf = {'sub': str(id_usuario), 'exp': data_expiracao}
    jwt_codificado = jwt.encode(dic_inf,SECRECT_KEY, ALGORITHM)
    return jwt_codificado

def autenticar_usuario(email, senha, session):
    usuario = session.query(Usuario).filter(Usuario.email==email).first()
    if not usuario:
        return False
    elif not bcrypt_context.verify(senha, usuario.senha):
        return False
    return usuario


