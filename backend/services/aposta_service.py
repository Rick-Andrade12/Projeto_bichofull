from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.aposta import Aposta
from models.carteira import Carteira
from services.sorteio_service import realizar_sorteio, conferir_aposta


def criar_aposta_service(session: Session, usuario_id: int, aposta_schema):
    carteira = session.query(Carteira).filter(Carteira.usuario_id == usuario_id).first()

    if not carteira:
        raise HTTPException(status_code=400, detail='carteira não encontrada')

    if aposta_schema.valor <= 0:
        raise HTTPException(status_code=400, detail='o valor da aposta deve ser maior que zero')

    if carteira.saldo < aposta_schema.valor:
        raise HTTPException(status_code=400, detail='saldo insuficiente')

    if aposta_schema.tipo not in ['grupo', 'milhar']:
        raise HTTPException(status_code=400, detail='tipo de aposta inválido')

    nova_aposta = Aposta(
        usuario_id=usuario_id,
        tipo=aposta_schema.tipo,
        numero=aposta_schema.numero,
        valor=aposta_schema.valor,
        status='pendente',
        premio=0.0
    )

    carteira.saldo -= aposta_schema.valor

    session.add(nova_aposta)
    session.commit()
    session.refresh(nova_aposta)
    session.refresh(carteira)

    novo_sorteio = realizar_sorteio(session)
    conferir_aposta(session, nova_aposta, novo_sorteio)

    session.refresh(nova_aposta)
    session.refresh(carteira)

    return {
    'mensagem': 'aposta realizada com sucesso',
    'aposta_id': nova_aposta.id,
    'tipo': nova_aposta.tipo,
    'numero_apostado': nova_aposta.numero,
    'valor_apostado': nova_aposta.valor,
    'status': nova_aposta.status,
    'premio': nova_aposta.premio,
    'posicao_premiada': nova_aposta.posicao_premiada,
    'saldo_atual': carteira.saldo,
    'rodada': novo_sorteio["rodada"],
    'sorteios': novo_sorteio["sorteios"]
}


def listar_apostas_service(session: Session, usuario_id: int):
    apostas = session.query(Aposta).filter(Aposta.usuario_id == usuario_id).all()
    return apostas


def historico_apostas_service(session: Session, usuario_id: int):
    apostas = session.query(Aposta).filter(
        Aposta.usuario_id == usuario_id,
        Aposta.status.in_(["ganhou", "perdeu"])
    ).all()

    return apostas