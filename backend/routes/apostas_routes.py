# from fastapi import APIRouter, Depends, HTTPException
# from models.usuario import Usuario
# from models.aposta import Aposta
# from models.carteira import Carteira
# from sqlalchemy.orm import Session
# from backend.dependencies import pegar_sessao, verificar_token
# from schemas import ApostaCreate, ApostaResposta
# from typing import List
# from services.sorteio_service import realizar_sorteio, conferir_aposta

# aposta_router = APIRouter(prefix='/apostas', tags=['apostas'])





# @aposta_router.post('/apostar')
# async def apostar(
#     aposta_schema: ApostaCreate,
#     session: Session = Depends(pegar_sessao),
#     usuario: Usuario = Depends(verificar_token)
# ):
#     carteira = session.query(Carteira).filter(Carteira.usuario_id == usuario.id).first()

#     if not carteira:
#         raise HTTPException(status_code=400, detail='carteira não encontrada')

#     if aposta_schema.valor <= 0:
#         raise HTTPException(status_code=400, detail='o valor da aposta deve ser maior que zero')

#     if carteira.saldo < aposta_schema.valor:
#         raise HTTPException(status_code=400, detail='saldo insuficiente')

#     if aposta_schema.tipo not in ['grupo', 'milhar']:
#         raise HTTPException(status_code=400, detail='tipo de aposta inválido')

#     nova_aposta = Aposta(
#         usuario_id=usuario.id,
#         tipo=aposta_schema.tipo,
#         numero=aposta_schema.numero,
#         valor=aposta_schema.valor,
#         status='pendente',
#         premio=0.0
#     )

#     carteira.saldo -= aposta_schema.valor

#     session.add(nova_aposta)
#     session.commit()
#     session.refresh(nova_aposta)
#     session.refresh(carteira)

#     novo_sorteio = realizar_sorteio(session)

#     conferir_aposta(session, nova_aposta, novo_sorteio)

#     session.refresh(nova_aposta)
#     session.refresh(carteira)

#     return {
#         'mensagem': 'aposta realizada com sucesso',
#         'aposta_id': nova_aposta.id,
#         'tipo': nova_aposta.tipo,
#         'numero_apostado': nova_aposta.numero,
#         'valor_apostado': nova_aposta.valor,
#         'status': nova_aposta.status,
#         'premio': nova_aposta.premio,
#         'saldo_atual': carteira.saldo,
#         'grupo_sorteado': novo_sorteio["grupo"],
#         'milhar_sorteada': novo_sorteio["milhar"],
#         'bicho_sorteado': novo_sorteio["bicho"]
#     }

# @aposta_router.get('/listar', response_model=List[ApostaResposta])
# async def listar_apostas(
#     session: Session = Depends(pegar_sessao),
#     usuario: Usuario = Depends(verificar_token)
# ):
#     apostas = session.query(Aposta).filter(Aposta.usuario_id == usuario.id).all()

#     return apostas

# @aposta_router.get('/historico', response_model=List[ApostaResposta])
# async def historico_apostas(
#     session: Session = Depends(pegar_sessao),
#     usuario: Usuario = Depends(verificar_token)
# ):
#     apostas = session.query(Aposta).filter(
#         Aposta.usuario_id == usuario.id,
#         Aposta.status.in_(["ganhou", "perdeu"])
#     ).all()

#     return apostas

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