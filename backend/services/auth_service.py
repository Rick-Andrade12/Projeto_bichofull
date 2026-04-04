from fastapi import HTTPException
from datetime import timedelta
from sqlalchemy.orm import Session

from models.usuario import Usuario
from models.carteira import Carteira
from security import bcrypt_context, criar_token, autenticar_usuario


def cadastrar_usuario_service(session: Session, usuariocreate):
    usuario = session.query(Usuario).filter(Usuario.email == usuariocreate.email).first()

    if usuario:
        raise HTTPException(status_code=400, detail='email ja cadastrado')

    senha_criptografada = bcrypt_context.hash(usuariocreate.senha)

    novo_usuario = Usuario(
        usuariocreate.nome,
        usuariocreate.email,
        senha_criptografada
    )

    session.add(novo_usuario)
    session.commit()
    session.refresh(novo_usuario)

    nova_carteira = Carteira(usuario_id=novo_usuario.id)
    session.add(nova_carteira)
    session.commit()

    return {'mensagem': 'cadastro feito'}


def login_usuario_service(session: Session, loginusuario):
    usuario = autenticar_usuario(loginusuario.email, loginusuario.senha, session)

    if not usuario:
        raise HTTPException(status_code=400, detail='usuario não encontrado')

    access_token = criar_token(usuario.id)
    refresh_token = criar_token(usuario.id, duracao_token=timedelta(days=7))

    return {
        'access_token': access_token,
        'refresh_token': refresh_token,
        'token_type': 'bearer'
    }


def login_form_service(session: Session, username: str, password: str):
    usuario = autenticar_usuario(username, password, session)

    if not usuario:
        raise HTTPException(status_code=400, detail='usuario não encontrado')

    access_token = criar_token(usuario.id)

    return {
        'access_token': access_token,
        'token_type': 'bearer'
    }


def refresh_token_service(usuario):
    access_token = criar_token(usuario.id)

    return {
        'access_token': access_token,
        'token_type': 'bearer'
    }