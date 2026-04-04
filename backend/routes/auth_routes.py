from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

from models.usuario import Usuario
from dependencies import pegar_sessao, verificar_token
from schemas.usuario_schema import UsuarioCreate,  UsuarioResposta
from schemas.auth_schema import LoginUsuario, TokenResposta
from services.auth_service import (
    cadastrar_usuario_service,
    login_usuario_service,
    login_form_service,
    refresh_token_service
)

auth_router = APIRouter(prefix='/auth', tags=['auth'])


@auth_router.post('/cadastrar')
async def cadastro(
    usuariocreate: UsuarioCreate,
    session: Session = Depends(pegar_sessao)
):
    return cadastrar_usuario_service(session, usuariocreate)


@auth_router.post('/login', response_model=TokenResposta)
async def login(
    loginusuario: LoginUsuario,
    session: Session = Depends(pegar_sessao)
):
    return login_usuario_service(session, loginusuario)


@auth_router.post('/login-form')
async def login_form(
    dados_formulario: OAuth2PasswordRequestForm = Depends(),
    session: Session = Depends(pegar_sessao)
):
    return login_form_service(
        session,
        dados_formulario.username,
        dados_formulario.password
    )


@auth_router.get('/refresh')
async def use_refresh(usuario: Usuario = Depends(verificar_token)):
    return refresh_token_service(usuario)


@auth_router.get('/me', response_model=UsuarioResposta)
async def buscar_usuario_logado(usuario: Usuario = Depends(verificar_token)):
    return usuario