# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.orm import Session

# from backend.dependencies import pegar_sessao, verificar_token
# from models import Carteira, Usuario
# from schemas import CarteiraResposta

# carteira_router = APIRouter(prefix='/carteira', tags=['carteira'])

# @carteira_router.get('/saldo', response_model=CarteiraResposta)
# async def ver_saldo(
#     session: Session = Depends(pegar_sessao),
#     usuario: Usuario = Depends(verificar_token)
# ):
#     carteira = session.query(Carteira).filter(Carteira.usuario_id == usuario.id).first()

#     if not carteira:
#         raise HTTPException(status_code=404, detail='carteira nao encontrada')

#     return carteira


from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from dependencies import pegar_sessao, verificar_token
from models.usuario import Usuario
from schemas.carteira_schema import CarteiraResposta
from services.carteira_service import buscar_saldo_service

carteira_router = APIRouter(prefix='/carteira', tags=['carteira'])


@carteira_router.get('/saldo', response_model=CarteiraResposta)
async def ver_saldo(
    session: Session = Depends(pegar_sessao),
    usuario: Usuario = Depends(verificar_token)
):
    return buscar_saldo_service(session, usuario.id)