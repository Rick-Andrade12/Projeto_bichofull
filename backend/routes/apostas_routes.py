from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from models.usuario import Usuario
from dependencies import pegar_sessao, verificar_token
from schemas.aposta_schema import ApostaCreate, ApostaResposta
from services.aposta_service import (
    criar_aposta_service,
    listar_apostas_service,
    historico_apostas_service
)

aposta_router = APIRouter(prefix='/apostas', tags=['apostas'])


@aposta_router.post('/apostar')
async def apostar(
    aposta_schema: ApostaCreate,
    session: Session = Depends(pegar_sessao),
    usuario: Usuario = Depends(verificar_token)
):
    return criar_aposta_service(session, usuario.id, aposta_schema)


@aposta_router.get('/listar', response_model=List[ApostaResposta])
async def listar_apostas(
    session: Session = Depends(pegar_sessao),
    usuario: Usuario = Depends(verificar_token)
):
    return listar_apostas_service(session, usuario.id)


@aposta_router.get('/historico', response_model=List[ApostaResposta])
async def historico_apostas(
    session: Session = Depends(pegar_sessao),
    usuario: Usuario = Depends(verificar_token)
):
    return historico_apostas_service(session, usuario.id)
