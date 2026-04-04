from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.carteira import Carteira


def buscar_saldo_service(session: Session, usuario_id: int):
    carteira = session.query(Carteira).filter(Carteira.usuario_id == usuario_id).first()

    if not carteira:
        raise HTTPException(status_code=404, detail='carteira nao encontrada')

    return carteira